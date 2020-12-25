from FolderClass import Folder
from PageClass import Page

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
        folderName = str(input("What shall the folder be called"))
        self.currentFolder.createFolder(folderName)

    def goBackAFolder(self):
        self.currentFolder = self.previousFolder

    def createFile(self):
        fileName = str(input("What shall the file be called"))
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
            if isinstance(page, Page):
                print(page.pageName)
                choices.append(page)


        pageChoice = int(input("Which page do you want to edit?"))
        choices[pageChoice].addCode()
        choices[pageChoice].showCode()

    def changeFolder(self):
        for folder in self.currentFolder.container:
            if isinstance(folder, Folder):
                print(folder.folderName)

        self.previousFolder = self.currentFolder
        self.currentFolder = self.currentFolder.container[int(input("Which Folder: "))]
