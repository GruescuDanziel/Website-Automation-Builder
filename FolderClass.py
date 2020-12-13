from PageClass import Page

class Folder:

    def __init__(self, folderName):
        self.folderName = folderName;
        self.container = []

    def createPage(self, pageName):
        self.container.append(Page(pageName))

    def createFolder(self, folderName):
        self.container.append(Folder(folderName))

    def viewFolders(self):
        for folder in self.container:
            if isinstance(folder, Folder):
                print(f"{folder.folderName} is in {self.folderName}")

            if isinstance(folder, Page):
                print(f"{folder.pageName}.html is a file")
