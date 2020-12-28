from FolderClass import Folder
from PageClass import Page
import questions as qs

class Website:
    
    def create(self):
        self.name = str(input("What will the website be called: "))
        self.code = ""
        self.mainFolder = Folder(self.name)
        self.currentFolder = self.mainFolder
        self.style = "Normal Dark"
        self.editing = True

    def getData(self):
        print(self.name)
    
    def createFolder(self):
        folderName = qs.inputQuestion()
        self.currentFolder.createFolder(folderName)

    def goBackAFolder(self):
        self.currentFolder = self.previousFolder

    def createFile(self):
        fileName = qs.inputQuestion()
        self.currentFolder.createPage(fileName)

    def checkEntireStructure(self):
        print(self.currentFolder.childFoldersNames)

    def checkCurrentFolder(self):
        self.currentFolder.viewFolders()

    def editFile(self):
        choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
        choiceFile = self.currentFolder.childFiles[choiceFileName]
        choiceFile.addCode()

    def checkFile(self):
        choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
        choiceFile = self.currentFolder.childFiles[choiceFileName]
        
        choiceFile.showCode()

    def removeCode(self):
        choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
        choiceFile = self.currentFolder.childFiles[choiceFileName]
        
        choiceFile.removeCode()

    def changeFolder(self):
        changeFolder = qs.listChoice(self.currentFolder.childFoldersNames)

        self.previousFolder = self.currentFolder
        self.currentFolder = self.currentFolder.childFolders[changeFolder]

    def endEditing(self):
        confirm = qs.confirmQuestion()
        if confirm:
            self.editing = False
        else:
            pass
