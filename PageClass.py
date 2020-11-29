
class File:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.code = []

    def addCode(self, newCode):
        self.code.append(newCode.code)

    def showCode(self):
        for code in self.code:
            print(code)

    def removeCode(self):
        index = 1
        for code in self.code:
            print(f"{index} - {code}")
            index += 1

        self.code[int(input("Which do you want to remove")) -1 ] = ""
