from CodeClass import Code

class Page:
    
    def __init__(self, pageName):
        self.pageName = pageName
        self.code = []
        self.startingCode = "<!DOCTYPE html> \n <html> \n <head> \n <body>"
        self.endingCode = "\n </body> \n  </html>"

    def addCode(self):
        dataToAdd= str(input("What will you want to add?"))
        tagType = str(input("What kind of tag?"))
        tagStyle = str(input("What style will it be?"))
        self.code.append(Code(dataToAdd, tagStyle, tagType).code)

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
