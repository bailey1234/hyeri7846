$(document).ready(function(){


	$('#example').tooltip();
	$('.popover-dismiss').popover({
		trigger: 'focus'
	});
	$('#loading-example-btn').click(function () {
		var btn = $(this);
		btn.button('loading');

	});

	$( "#target" ).focus(function() {
		alert( "Handler for .focus() called.");




	});


	$( "#target" ).keydown(function() {
		alert("Handler for .keydown() called." );
	});

});


