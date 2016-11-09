import json

def getBaseDir():
   return '/home/nfang/git/projects/webScraping/projectEuler/'

def getSettingsFile():
   return getBaseDir() + "settings.json"

def loadSettings():
   settingsFilePtr = open(getSettingsFile(),'r')
   settings = json.load(settingsFilePtr)
   settingsFilePtr.close()
   return settings

def getProblemNumberString(number): 
   if (number < 10):
      return '00' + str(number)
   elif (number < 100):
      return '0' + str(number)
   else:
      return str(number)

def setNextProblemNumber(number):
   settings = loadSettings()
   settingsFilePtr = open(getSettingsFile(), 'w')
   settings['projectEuler']['nextProblemNumber'] = number
   if settings:
      json.dump(settings,settingsFilePtr)
   settingsFilePtr.close()
