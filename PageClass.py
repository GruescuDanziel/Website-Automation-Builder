
class File:
    
    def __init__(self, fileName, fileType):
        self.fileName = fileName
        self.fileType = fileType
        self.code = []

    def addCode(self, newCode):
        self.code.append(newCode.code)

    def showCode(self):
        for code in self.code:
            print(code)

