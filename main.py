from WebsiteClass import Website
import questions as qs

initialAction = int(input("What do you wish to do: 1. Make a new webSite. 2. Edit an old save"))
posibleChoices = ['getData', 'createFolder', 'goBackAFolder','createFile', 'checkEntireStructure', 'checkCurrentFolder', 'editFile','checkFile', 'removeCode', 'changeFolder', 'endEditing']


if initialAction == 1:
    newWebsite = Website()
    newWebsite.create()
    while(newWebsite.editing):
        userChoice = qs.listChoice(posibleChoices)
        getattr(newWebsite, userChoice)()
