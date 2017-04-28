// When the keyword "this" is inside of a declared object

// strict mode does not make a difference here

var person = {
	firstName: "Elie",
	sayHi: function() {
		return "Hi " + this.firstName
	},
	determineContext: function() {
		return this === person
	}
}

person.sayHi() // "Hi Elie"

person.determineContext() // true