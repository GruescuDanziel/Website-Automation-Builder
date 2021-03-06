from CodeClass import Code
import questions as qs

class Page:
    
    def __init__(self, pageName):
        self.pageName = pageName
        self.code = {}
        self.codeList = []
        self.startingCode = "<!DOCTYPE html> \n <html> \n <head> \n <body>"
        self.endingCode = "\n </body> \n  </html>"

    def addCode(self):
        dataToAdd = qs.editQuestion("").rstrip()
        tagType = qs.inputQuestion()
        tagStyle = qs.inputQuestion()
        self.code[f'{dataToAdd[0:10]}...'] = Code(dataToAdd, tagStyle, tagType)
        self.codeList.append(f'{dataToAdd[0:10]}...')

    def showCode(self):
        print(self.startingCode)
        for code in self.codeList:
            print(self.code[code].code)

        print(self.endingCode)

    def editCode(self):
        codeToEdit = qs.listChoice(self.codeList)
        indexToChange = self.codeList.index(codeToEdit)
        self.code[codeToEdit].data = qs.editQuestion(self.code[codeToEdit].data).rstrip()
        nameOfEdit = self.code[codeToEdit].data[0:10]
        self.codeList[indexToChange] = f"{nameOfEdit}..."
        self.code[f"{nameOfEdit}..."] = self.code[codeToEdit]
        self.code[f"{nameOfEdit}..."].regenerateCode()
        del self.code[codeToEdit]
        

    def removeCode(self):
        codeToRemove = qs.listChoice(self.codeList)
        del self.code[codeToRemove]
        self.codeList.remove(codeToRemove)
