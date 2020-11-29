from FolderClass import Folder

class Website:
    
    def create(self):
        self.name = str(input("What will the website be called: "))
        self.code = ""
        self.mainFolder = Folder(self.name)
        self.currentFolder = self.mainFolder

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

    def changeFolder(self):
        for folder in self.currentFolder.container:
            print(folder.folderName)

        self.previousFolder = self.currentFolder
        self.currentFolder = self.currentFolder.container[int(input("Which Folder: "))]
