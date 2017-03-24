$(document).ready(function() {
	$(".connect_match").click(function() {
		var $this = $(this);
		var match_link = $this.data("marathonlink");
		$.ajax({
			type: 'GET',
			url: '/harbs/open_match/',
			data: { match_link: match_link }
		});
	});
	
	$("#generate_page").click(function() {
		$.ajax({
			type: 'GET',
			url: 'https://localhost:443/harbs/generate_page/'
		});
	});

	$("#refresh_matchlist").click(function() {
		$.ajax({
			type: 'GET',
			url: 'https://localhost:443/harbs/match_list/'
		});
	});
});