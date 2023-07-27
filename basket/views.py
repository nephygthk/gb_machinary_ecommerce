from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .basket import Basket
from store.models import Product
from account.forms import ClientForm
from order.models import Order, OrderItem
from frontend import emails


def basket_summary(request):
    basket = Basket(request)
    form = ClientForm()
    return render(request, 'basket/summary.html', {'basket': basket, 'form':form})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        qty = int(request.POST.get('qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response
    

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
    

def checkout_order(request):
    basket = Basket(request)
    form = ClientForm(request.POST)
    if form.is_valid():
        customer = form.save()
        baskettotal = basket.get_total_price()
        basketsubtotal = basket.get_subtotal_price()
        
        if request.user.is_authenticated:
            user_id = request.user.id
            order = Order.objects.create(user_id=user_id, full_name=customer.c_full_name, 
                    email=customer.   c_email, country=customer.c_country, city=customer.c_city, total=baskettotal, sub_total=basketsubtotal)
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
        else:
            order = Order.objects.create(full_name=customer.c_full_name, 
                    email=customer.   c_email, country=customer.c_country, total=baskettotal, sub_total=basketsubtotal)
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        f_message = emails.final_message2(
                                    customer.c_full_name, order.order_key,
                                    order.created, customer.c_country,
                                    customer.c_city, basket.get_total_price()
                                    )
        try:
            emails.email_message_send(
                'Order Successful',
                f_message,
                customer.c_email,
            )
        except:
            pass 
        finally:
            return redirect('basket:order_successful')
    else:
        messages.error(request, 'Something went wrong, please check the form informations and try again')
        return redirect('basket:basket_summary')
    

def order_successful(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'basket/order_successful.html')
    
