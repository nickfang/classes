# file=open("testing.txt",'w')

# file.close()

import os
# dir(os)
# dir(os.path)
# help(os.path)

print(os.getcwd())

os.chdir("c:\\users\\nfang\\repos\\classes\\udemy\\pythinbuilddataanalysisprogram")

os.makedirs

# to allow for cross platform
fullpath = ""
filename=os.path.basename(fullpath)

#only filename
os.path.splitext(filename)[0]
#only extension
os.path.splitext(filename)[1]

if not os.path.exists(fullpath):
	os.makedirs(fullpath)

with open("testing.txt",'w') as file:
	file.write("the with method!")


os.rename("testing.txt","test.txt")
os.rename("test.txt","text.csv")

name=os.path.splitext(filename)[0]
newname=nae+".txt"
os.rename(filename,newname)

import glob
gzlist=glob.glob("*.gz")

for file in gzlist:
	filename=os.path.splitext(file)[0]
	newname=filename+".zip"
	os.rename(file,newname)

