import os
from shutil import copyfile

def getTemplate(problemNumber, src="webScraping\\problemTemplates", dest="python"):
	templateFile = os.path.join(src, problemNumber)
	if os.path.isFile(templateFile):
		copyfile(os.path.join(src, problemNumber), os.path.join(dest, problemNumber))
	else:
		print("Template file " + templateFile + " does not exist.")

# if __name__ == "__main__":
