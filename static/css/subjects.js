window.onresize = function() {
    location.reload();
}

//owl carousel
$(".carousel").owlCarousel({
    margin: 0,
    loop: true,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 3,
            nav: true
        },
        600: {
            items: 4,
            nav: true
        },
        700: {
            items: 5,
            nav: true
        },
        1000: {
            items: 5,
            nav: true
        }
    }
});