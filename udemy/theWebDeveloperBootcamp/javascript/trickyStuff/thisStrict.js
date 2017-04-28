"use strict"

console.log(this); //window

function whatIsThis() {
	return this;
}

function variableInThis() {
	// since we are in strict mode this is undefined
	// so what happens if we add a property on undefined?
	// let's see what happens when we call the function...
	this.person = "Elie"
}

variableInThis() // TypeError, can't set person on undefined!

whatIsThis() // undefined