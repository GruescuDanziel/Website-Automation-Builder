from CodeClass import Code
import questions as qs

class Page:
    
    def __init__(self, pageName):
        self.pageName = pageName
        self.code = {}
        self.codeList = []
        #f'{dataToAdd[0:10]}...'
        self.startingCode = "<!DOCTYPE html> \n <html> \n <head> \n <body>"
        self.endingCode = "\n </body> \n  </html>"

    def addCode(self):
        dataToAdd = qs.editQuestion() 
        tagType = qs.inputQuestion()
        tagStyle = qs.inputQuestion()
        self.code[f'{dataToAdd[0:10]}...'] = Code(dataToAdd, tagStyle, tagType)
        self.codeList.append(f'{dataToAdd[0:10]}...')

    def showCode(self):
        print(self.startingCode)
        for code in self.codeList:
            print(self.code[code].code)

        print(self.endingCode)

    def removeCode(self):
        codeToRemove = qs.listChoice(self.codeList)
        del self.code[codeToRemove]
