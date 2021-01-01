from PageClass import Page

class Folder:

    def __init__(self, folderName, folderRank=-1):
        self.folderName = folderName;
        
        self.childFolders= {}
        self.childFoldersNames = []

        self.childFiles = {}
        self.childFilesNames = []
        self.folderRank = folderRank + 1

    def createPage(self, pageName):
        self.childFiles[pageName] = Page(pageName)
        self.childFilesNames.append(pageName)

    def createFolder(self, folderName, folderRank=0):
        self.childFolders[folderName] = Folder(folderName,folderRank)
        self.childFoldersNames.append(folderName)

    def viewFolders(self):
        print(' '*self.folderRank+'-'+self.folderName)
        if len(self.childFoldersNames) != 0:
            for folder in self.childFoldersNames:
                self.childFolders[folder].viewFolders()
