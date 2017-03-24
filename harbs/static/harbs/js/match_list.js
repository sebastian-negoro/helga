$(document).ready(function() {
	$("#banners_block").remove();

	var matchlist = [];

	function send_matchlist() {
		alert('UB!');
		matchlist = $('.label[data-reactid*=22723]').each(function() {
			hrefs.push($(this).attr('href'));
		});		
		json_matchlist = JSON.stringify(matchlist);

		$.ajax({
			type: 'GET',
			url: 'https://localhost:443/harbs/match_list/',
			data: { json_matchlist: json_matchlist }
		});
	}

	$('#timer').click(function() {
		setInterval(send_matchlist, 20000);
	});
});