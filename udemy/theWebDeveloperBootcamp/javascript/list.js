var todos = [];

var input = prompt("What would you like to do?");

while (input !== "quit") {
	if (input === "list") {
		console.log("**********");
		todos.forEach(function(todo, index) {
			console.log(index + ": " + todo);
		});
		console.log("**********");
	} else if (input === "new") {
		var newTodo = prompt("Enter new todo");
		todos.push(newTodo);
		console.log("Added Todo");
	} else if (input === "delete") {
		index = prompt("Enter index of todo to delete");
		todos.splice(index, 1);
	}
	input = prompt("What would you like to do?");
}

console.log("ok, you quit the app");