#!/usr/bin/python

import os
import re
from BeautifulSoup import BeautifulSoup
from localToolbox import loadSettings, getBaseDir

def getDescription(htmlFileName):
   content = open(htmlFileName,'r').read()
   soup = BeautifulSoup(content)
   
   # add the name of the problem
   problemDescription = '# ' + str(soup.find('h2'))[4:-5] + '\n\n'
   # add the description of the problem
   webDescription = soup.find('div',attrs={'class':'problem_content'})#.findAll('p')
   problemDescription += re.sub(r'^',r'#',str(webDescription),flags=re.MULTILINE) + '\n\n'
   # maintain fractions
   problemDescription = re.sub(r'\<sup\>(.*)\<\/sup\>(.*)\<sub\>(.*)\<\/sub\>', r'\1\2\3',problemDescription)
   # replace power with carat
   problemDescription = re.sub(r'\<sup\>([0-9].+)\<\/sup\>', r'^\1', problemDescription)
   # move definition and external link to () after word
   problemDescription = re.sub(r'\<dfn title="(.*?)"\>(.*?)\<\/dfn\>', r'\2 (\1)', problemDescription)
   problemDescription = re.sub(r'\<a href="(http:.*?)"\>(.*?)\<\/a\>', r'\2 (\1)', problemDescription)
   # remove link to another problem
   problemDescription = re.sub(r'\<a href="problem=.*?"\>(Problem.*?)\<\/a\>', r'\1', problemDescription)
   # remove simple tags
   problemDescription = re.sub(r'\<(|\/)(u|var|i|sup|sub|b|em|strong)\>', r'', problemDescription)
   problemDescription = re.sub(r'\<(|\/)(div.*?|p.*?|span.*?|font.*?)\>', r'', problemDescription)
   # remove end tags
   problemDescription = re.sub(r'\<br.*?\>', '', problemDescription)
   
   # check to see if there are any tags left that I need to process.
   #tags = re.findall(r'\<.*?\>',problemDescription)
   #for x in tags:
   #   print(htmlFileName + ': ' + str(x))

   return problemDescription
   
def createProblemFile(description):
   contentToWrite = description
   contentToWrite += 'import time\n\nstartTime = time.time()\n\n\n\n'
   contentToWrite += 'print(\'Elapsed time: \' + str(time.time()-startTime))'
   return contentToWrite

baseDir = getBaseDir()
fileList = os.listdir(baseDir + 'rawHTML')
fileList.sort()
for htmlFileName in fileList:
   content = createProblemFile(getDescription('rawHTML/' + htmlFileName))
   outputFileName = 'problemTemplates/' + re.search(r'[0-9]{3}',htmlFileName).group(0) + '.py'
   print('Creating: ' + outputFileName) 
   with open(baseDir + outputFileName, 'w') as fileWritePtr:
      fileWritePtr.write(content)
   fileWritePtr.closed
 
