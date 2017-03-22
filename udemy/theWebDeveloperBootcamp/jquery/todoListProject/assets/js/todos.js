// Check off specific todo's by clicking.
$("ul").on("click", "li", function() {
	$(this).toggleClass("completed");
});

// click on x to delete Todo
$("ul").on("click", "span", function(e) {
	$(this).parent().fadeOut(500, $(this).remove);
	e.stopPropagation();
});

$("input[type='text']").keypress(function(e) {
	if (e.which === 13) {
		// grabbing new todo text from input
		console.log();
		var todoText = $(this).val();
		$(this).val();
		//
		$("ul").append(`<li><span><i class="fa fa-trash"></i></span> ${todoText}</li>`);
	}
});

$(".fa-plus").click(function() {
	$("input[type='text']").fadeToggle();
})