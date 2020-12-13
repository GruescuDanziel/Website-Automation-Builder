from FolderClass import Folder
from PageClass import File

class Website:
    
    def create(self):
        self.name = str(input("What will the website be called: "))
        self.code = ""
        self.mainFolder = Folder(self.name)
        self.currentFolder = self.mainFolder
        self.style = "Normal Dark"

    def getData(self):
        print(self.name)
    
    def createFolder(self, folderName):
        self.currentFolder.createFolder(folderName)

    def goBackAFolder(self):
        self.currentFolder = self.previousFolder

    def createFile(self,fileName):
        self.currentFolder.createPage(fileName)

    def checkEntireStructure(self):
        for folder in self.mainFolder.container:
            if isinstance(folder, Folder):
                folder.viewFolders()

    def checkCurrentFolder(self):
        self.currentFolder.viewFolders()

    def editFile(self):
        choices = []
        for page in self.currentFolder.container:
            if isinstance(page, File):
                print(page.fileName)
                choices.append(page)


        pageChoice = int(input("Which page do you want to edit?"))
        choices[pageChoice].addCode('ads')
        choices[pageChoice].showCode()

    def changeFolder(self):
        for folder in self.currentFolder.container:
            if isinstance(folder, Folder):
                print(folder.folderName)

        self.previousFolder = self.currentFolder
        self.currentFolder = self.currentFolder.container[int(input("Which Folder: "))]
