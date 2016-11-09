#!/usr/bin/python

import re
import json
import urllib2
from BeautifulSoup import BeautifulSoup
from localToolbox import getBaseDir, loadSettings, getProblemNumberString, setNextProblemNumber

settings = loadSettings()
filenameTemplate = settings['projectEuler']['filenameTemplate']
number = settings['projectEuler']['nextProblemNumber']
lastNumber = settings['projectEuler']['lastProblemNumber']
urlBase = settings['projectEuler']['baseURL']

if number > lastNumber:
   quit()

fileName = re.sub('xxx', getProblemNumberString(number), filenameTemplate)
fileName = getBaseDir() + fileName
with open(fileName, 'w') as fileWritePtr:
   content = urllib2.urlopen(urlBase + str(number)).read()
   fileWritePtr.write(str(content))
fileWritePtr.closed

#check that something was written into the file.
with open(fileName, 'r') as fileReadPtr:
   content = fileReadPtr.read()
   soup = BeautifulSoup(content)
   if soup.html.head.title.string == 'Problem ' + str(number) + ' - Project Euler':
      setNextProblemNumber(number + 1)
   else:
      print('nothing downloaded')
      #TODO: figure out how to throw errors in python
fileReadPtr.closed

#TODO: figure out what accessing too quickly looks like.  Create error condition based on that.
