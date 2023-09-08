$(document).ready(function () {
    const owl = $(".banner-carousal").owlCarousel({
        items: 1,
        loop: true,
        lazyLoad: true,
        margin: 10,
        autoplay: true,
        dots: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsiveClass: true,
    });
    $('#nextBtn').click(function () {
        owl.trigger('next.owl.carousel');
    });
    $('#prevBtn').click(function () {
        owl.trigger('prev.owl.carousel');
    });
    const owl2 = $(".team-carousal").owlCarousel({
        items: 3,
        loop: true,
        lazyLoad: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },

            768: {
                items: 2,
            },

            1024: {
                items: 3,
            }
        }
    });
    $('#nextBtn2').click(function () {
        owl2.trigger('next.owl.carousel');
    });
    $('#prevBtn2').click(function () {
        owl2.trigger('prev.owl.carousel');
    });
    $('#nextBtnv2').click(function () {
        owl2.trigger('next.owl.carousel');
    });
    $('#prevBtnv2').click(function () {
        owl2.trigger('prev.owl.carousel');
    });
});

