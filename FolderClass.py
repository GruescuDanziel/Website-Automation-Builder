from PageClass import File

class Folder:

    def __init__(self, folderName):
        self.folderName = folderName;
        self.container = []

    def createPage(self, pageName):
        self.container.append(File(pageName))

    def createFolder(self, folderName):
        self.container.append(Folder(folderName))

    def viewFolders(self):
        for folder in self.container:
            if isinstance(folder, Folder):
                print(f"{folder.folderName} is in {self.folderName}")

            if isinstance(folder, File):
                print(f"{folder.fileName}.html is a file")
