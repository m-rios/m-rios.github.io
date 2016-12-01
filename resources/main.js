$(document).ready(function(){
	var $ = jQuery.noConflict();

	$(function() {
		$('a[href*="#"]:not([href="#"])').click(function() {
			if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
				var target = $(this.hash);
				target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
				if (target.length) {
					$('html, body').animate({
						scrollTop: target.offset().top
					}, 800);
					return false;
				}
			}
		});
	});

	var landing_end = $("#landing").height() - $(".header").height();

	$(window).on("scroll", function () {
		if ($(this).scrollTop() > landing_end ) {
			$("#puta").addClass("fill");
		}
		else {
			$("#puta").removeClass("fill");
		}
	});

});