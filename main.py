from WebsiteClass import Website
import questions as qs

initialChoices = ['New Website', 'Load Website']
initialAction = qs.listChoice(initialChoices)
posibleChoices = ['createFolder', 'goBackAFolder',
        'createFile', 'checkEntireStructure', 'checkCurrentFolder', 
        'editCode','addCode','checkFile', 'removeCode', 'changeFolder', 'endEditing',]

folderRelatedCommands    = ['createFolder', 'goBackAFolder', 'checkCurrentFolder', 'changeFolder']
fileRelatedCommands      = ['createFile', 'checkFile', 'addCode', 'removeCode', 'editCode']
otherRelatedCommands     = ['checkEntireStructure', 'endEditing']

dicitionaryOfChoiches = {
        'folderRelated'    : folderRelatedCommands,
        'fileRelated'      : fileRelatedCommands,
        'other'            : otherRelatedCommands
        }

if initialAction == 'New Website':
    newWebsite = Website()
    newWebsite.create()
    while(newWebsite.editing):
        userChoice = qs.expandMenu(dicitionaryOfChoiches)
        getattr(newWebsite, userChoice)()
