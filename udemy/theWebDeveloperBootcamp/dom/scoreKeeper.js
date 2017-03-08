const numInput = document.querySelector("input");
const p1Button = document.querySelector("#p1");
const p2Button = document.getElementById("p2");
const reset = document.querySelector("#reset");
const p1Display = document.querySelector("#p1-display");
const p2Display = document.querySelector("#p2-display");
const winningScoreDisplay = document.querySelector("#max-score-display");
let p1Score = 0;
let p2Score = 0;
let gameOver = false;
let winningScore = 5;

function resetGame() {
	p1Score = 0;
	p2Score = 0;
	p1Display.textContent = 0;
	p2Display.textContent = 0;
	p1Display.classList.remove("winner");
	p2Display.classList.remove("winner");
	gameOver = false;
	console.log("reset");
}


numInput.addEventListener("change", function() {
	resetGame();
	winningScoreDisplay.textContent = numInput.value;
	winningScore = Number(numInput.value);
});

p1Button.addEventListener("click", function() {
	if (!gameOver) {
		p1Score++;
		if (p1Score === winningScore) {
			gameOver = true;
			p1Display.classList.add("winner");
		}
		p1Display.textContent = p1Score;

	}
});

p2Button.addEventListener("click", function() {
	if (!gameOver) {
		p2Score++;
		if (p2Score === winningScore) {
			gameOver = true;
			p2Display.classList.add("winner");
		}
		p2Display.textContent = p2Score;
	}
});

reset.addEventListener("click", function() {
	resetGame();
})

