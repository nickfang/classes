const colorBox = document.querySelector(".color-box");
const button = document.querySelector("button");

function toggleColor() {
	colorBox.classList.toggle("green-color")
}

button.addEventListener("mouseup", toggleColor)


// colorBox.style.background = "blue";