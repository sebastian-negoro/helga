$(document).ready(function() {

	$("#send_ajax").click(function() {
		$.ajax({
			type: 'GET',
			dataType: 'JSON',
			url: 'https://127.0.0.1:443/harbs/send_test_ajax/',
			data: {test_msg: '88'},
			success: function(response) {
				$("#result").html(response);
			},
			error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        	}
		});
	});

	function send_time() {
		current_time = new Date($.now());
		$.ajax({
			type: 'GET',
			dataType: 'JSON',
			url: 'https://127.0.0.1:443/harbs/send_current_time/',
			data: {current_time: current_time},
			success: function(response) {
				$("#result").html(response);
			},
			error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        	}
		});
	}

	setInterval(send_time, 5000);
});