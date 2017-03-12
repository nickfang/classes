var colors = generateRandomColors(6);

const squares = document.querySelectorAll(".square");
var pickedColor = pickColor();
var colorDisplay = document.getElementById("colorDisplay");
var messageDisplay = document.querySelector("#message");
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#reset");

resetButton.addEventListener("click", function () {
	colors = generateRandomColors(6);
	pickedColor = pickColor();
	colorDisplay.textContent = pickedColor;
	for (var i = 0; i < squares.length; i++) {
		squares[i].style.background = colors[i];
	}
	h1.style.background = "#232323";
})

colorDisplay.textContent = pickedColor;

for (var i = 0; i < squares.length; i++) {
	// add initial colors to squares
	squares[i] .style.background = colors[i];

	// add click listeners to square
	squares[i].addEventListener("click", function() {
		//grab color of clicked square
		var clickedColor = this.style.background;
		if (clickedColor === pickedColor) {
			messageDisplay.textContent = "Correct";
			changeColors(pickedColor);
			h1.style.background = pickedColor;
			resetButton.textContent = "Play Again?";
		} else {
			this.style.background = "#232323";
			messageDisplay.textContent = "Try Again";
		}
	});
}

function changeColors(color) {
	squares.forEach( (square) => {
		square.style.background = color;
	});
}

function pickColor() {
	var random = Math.floor(Math.random() * colors.length);;
	return colors[random];
}

function generateRandomColors(num) {
	var arr = [];
	for (var i = 0; i < num; i++) {
		arr.push(randomColor());
	}
	return arr;
}

function randomColor() {
	var red = Math.floor(Math.random() * 256);
	var green = Math.floor(Math.random() * 256);
	var blue = Math.floor(Math.random() * 256);
	return "rgb(" + red + ", " + green + ", " + blue + ")";
}