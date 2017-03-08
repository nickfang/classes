var obj = {
	name: "chuck",
	age: 45,
	isCool: false,
	friends: ["bob", "tina"],
	add: function(x,y) {
		return x + y;
	}
}

console.log(obj.add(10,5));

// namespace collision

function speak() {
	return "Woof";
}

function speak() {
	return "meow";
}

console.log(speak());

// can't access "Woof" now

var dogSpace = {};
dogSpace.speak = function () {
	return "woof";
}

var catSpace = {}
catSpace.speak = function () {
	return "meow";
}

console.log(dogSpace.speak());
console.log(catSpace.speak());

// popular js library underscore.js
// keyword this

var comments = {};
comments.data = ["good job!", "bye", "lame..."];
function print(arr) {
	arr.forEach(function(el) {
		console.log(el);
	}
)}

print(comments.data);

// update comments using this keyword.

comments.print = function() {
	this.data.forEach(function(el) {
		console.log(el);
	})
}

comments.print();