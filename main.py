from WebsiteClass import Website

initialAction = int(input("What do you wish to do: 1. Make a new webSite. 2. Edit an old save"))
posibleChoices = ['getData', 'createFolder', 'goBackAFolder','createFile', 'checkEntireStructure', 'checkCurrentFolder', 'editFile', 'changeFolder', 'endEditing']

def makeChoice():
    index = 1
    for choice in posibleChoices:
        print(f'{index} - {choice}')
        index += 1
    return posibleChoices[int(input("Which one will you chose?"))-1]




if initialAction == 1:
    newWebsite = Website()
    newWebsite.create()
    while(newWebsite.editing):
        userChoice = makeChoice()
        getattr(newWebsite, userChoice)()
