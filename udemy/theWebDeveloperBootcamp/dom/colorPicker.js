var numSquares = 6;
var colors = [];
var pickedColor;
const h1 = document.querySelector("h1");
const colorDisplay = document.getElementById("colorDisplay");
const resetButton = document.querySelector("#reset");
const messageDisplay = document.querySelector("#message");
const modeButtons = document.querySelectorAll(".mode");
const squares = document.querySelectorAll(".square");

init();

function init() {
	resetButton.addEventListener("click", reset);
	modeButtons.forEach( (button) => {
		button.addEventListener("click", () => {
			modeButtons[0].classList.remove("selected");
			modeButtons[1].classList.remove("selected");
			button.classList.add("selected");
			button.textContent === "Easy" ? numSquares = 3 : numSquares = 6;
			reset();
		});
	});

	squares.forEach( (square) => {
		// add click listeners to square
		square.addEventListener("click", () => {
			//grab color of clicked square
			var clickedColor = square.style.background;
			if (clickedColor === pickedColor) {
				messageDisplay.textContent = "Correct";
				changeColors(pickedColor);
				h1.style.background = pickedColor;
				resetButton.textContent = "Play Again?";
			} else {
				square.style.background = "#232323";
				messageDisplay.textContent = "Try Again";
			}
		});
	});

	reset();
}

function reset() {
	colors = generateRandomColors(numSquares);
	pickedColor = pickColor();
	colorDisplay.textContent = pickedColor;
	squares.forEach( (square, i) => {
		if (colors[i]) {
			square.style.display = "block";
			square.style.background = colors[i];
		} else {
			square.style.display = "none";
		}
	});
	h1.style.background = "steelblue";
	messageDisplay.textContent = "";
	resetButton.textContent = "New Colors";
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