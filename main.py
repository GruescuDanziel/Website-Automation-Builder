from WebsiteClass import Website
import questions as qs

initialChoices = ['New Website', 'Load Website']
initialAction = qs.listChoice(initialChoices)
posibleChoices = ['getData', 'createFolder', 'goBackAFolder',
        'createFile', 'checkEntireStructure', 'checkCurrentFolder', 
        'editCode','addCode','checkFile', 'removeCode', 'changeFolder', 'endEditing',]


if initialAction == 'New Website':
    newWebsite = Website()
    newWebsite.create()
    while(newWebsite.editing):
        userChoice = qs.listChoice(posibleChoices)
        getattr(newWebsite, userChoice)()
