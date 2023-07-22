const myNabBar = document.querySelector('.navbar')

window.onscroll = function() {
    if (document.body.scrollTop >= 280 || document.documentElement.scrollTop >= 280) {
        myNabBar.classList.remove("scroll2");
        myNabBar.classList.add("scroll");
    } else {
      myNabBar.classList.remove("scroll");
      myNabBar.classList.add("scroll2");
    }
  };