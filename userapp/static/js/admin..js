 $('.drop').click(function () {
        $(this).toggleClass('open').siblings().removeClass('open');
    })



    $('.drop-menu li').each(function() {
    var delay = $(this).index() * 100 + 'ms';

    $(this).css({
        '-webkit-transition-delay': delay,
        '-moz-transition-delay': delay,
        '-o-transition-delay': delay,
        'transition-delay': delay
    });                  
});



$('.read-reviews-btn').click(function() {
	$('.read-reviews').slideDown();
});


$('.close-reviews').click(function() {
	$('.read-reviews').slideUp();
});

$('.mobile-menu ').click(function() {
	$('#sidebar').slideToggle();
});

$('.search-form .fa-search').click(function() {
	$('.search-form .form-control').slideToggle();
});