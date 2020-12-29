from FolderClass import Folder
from PageClass import Page
import questions as qs

class Website:
    
    def create(self):
        self.name = qs.inputQuestion()
        self.code = ""
        self.mainFolder = Folder(self.name)
        self.currentFolder = self.mainFolder
        self.style = "Normal Dark"
        self.editing = True

    def createFolder(self):
        folderName = ""
        while len(folderName) == 0:
            folderName = qs.inputQuestion()
        self.currentFolder.createFolder(folderName)

    def goBackAFolder(self):
        if self.currentFolder != self.name:
            self.currentFolder = self.previousFolder
        else:
            print("You are already at the root folder")

    def createFile(self):
        fileName = qs.inputQuestion()
        self.currentFolder.createPage(fileName)

    def checkEntireStructure(self):
        print(self.currentFolder.childFoldersNames)

    def checkCurrentFolder(self):
        self.currentFolder.viewFolders()

    def addCode(self):
        if len(self.currentFolder.childFilesNames) > 0:
            choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
            choiceFile = self.currentFolder.childFiles[choiceFileName]
            choiceFile.addCode()
        else:
            print("You have no files")

    def checkFile(self):
        if len(self.currentFolder.childFilesNames) > 0:
            choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
            choiceFile = self.currentFolder.childFiles[choiceFileName]
            choiceFile.showCode()
        else:
            print("You have no files")

    def editCode(self):
        if len(self.currentFolder.childFilesNames) > 0:
            choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
            choiceFile = self.currentFolder.childFiles[choiceFileName]
            choiceFile.editCode()
        else:
            print("You have no files")

    def removeCode(self):
        if len(self.currentFolder.childFilesNames) > 0:
            choiceFileName = qs.listChoice(self.currentFolder.childFilesNames)
            choiceFile = self.currentFolder.childFiles[choiceFileName]
            choiceFile.removeCode()
        else:
            print("You have no files")

    def changeFolder(self):
        if len(self.currentFolder.childFilesNames) > 0:
            changeFolder = qs.listChoice(self.currentFolder.childFoldersNames)
            self.previousFolder = self.currentFolder
            self.currentFolder = self.currentFolder.childFolders[changeFolder]
        else:
            print("You have no other folders in here")

    def endEditing(self):
        confirm = qs.confirmQuestion()
        if confirm:
            self.editing = False
        else:
            pass
