from PageClass import Page

class Folder:

    def __init__(self, folderName):
        self.folderName = folderName;
        
        self.childFolders= {}
        self.childFoldersNames = []

        self.childFiles = {}
        self.childFilesNames = []

    def createPage(self, pageName):
        self.childFiles[pageName] = Page(pageName)
        self.childFilesNames.append(pageName)

    def createFolder(self, folderName):
        self.childFolders[folderName] = Folder(folderName)
        self.childFoldersNames.append(folderName)

    def viewFolders(self):
        print(self.folderName)
        for folder in self.childFoldersNames:
            print(f"{folder} is in {self.folderName}")
