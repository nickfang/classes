console.log(this); //window

function whatIsThis() {
	return this;
}

function variableInThis() {
	// since the value of this is the window
	// all we are doing here is createing a global variable
	this.person = "Elie"
}

variableInThis() // Elie

whatIsThis() // window