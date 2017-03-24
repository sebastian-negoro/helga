$(document).ready(function() {

	function send_coefs_ajax() {
		//coefs = $('.height-column-with-price').first().attr('data-market-type');
		//coefs = $.map($('.height-column-with-price'), function(el) { return { value:'{\'bet_category\': ' + $(el).data('sel').mn + ',\'bet_name\': ' + $(el).data('sel').sn + ',\'bet_coef\': ' + $(el).data('sel').epr + '}' } });
		$.ajax({
			type: 'GET',
			dataType: 'JSON',
			crossDomain: true,
			url: 'https://localhost:443/harbs/send_coefs_ajax/',
			data: {json_coefs: '88'}
		});
	}

	send_coefs_ajax();
	setInterval(send_coefs_ajax, 5000);
});