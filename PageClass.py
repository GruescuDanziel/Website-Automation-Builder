from CodeClass import Code

class Page:
    
    def __init__(self, pageName):
        self.pageName = pageName
        self.code = []
        self.startingCode = "<!DOCTYPE html> \n <html> \n <head> \n <body>"
        self.endingCode = "\n </body> \n  </html>"

    def addCode(self, newCode):
        self.code.append(Code(content=newCode).code)

    def showCode(self):
        print(self.startingCode)
        for code in self.code:
            print(code)

        print(self.endingCode)

    def removeCode(self):
        index = 1
        for code in self.code:
            print(f"{index} - {code}")
            index += 1

        self.code[int(input("Which do you want to remove")) -1 ] = ""
