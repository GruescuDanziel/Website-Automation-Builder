class Code:
    def __init__(self, content,tagStyle="dark",tagType='h1',):
        self.data = content
        self.tagStyle = tagStyle
        self.tagType = tagType
        self.code = f"<{tagType} class='{tagStyle}'>"
        self.code += content
        self.code += f"</{tagType}>"

    def regenerateCode(self):
        self.code = f"<{self.tagType} class='{self.tagStyle}'>"
        self.code += self.data
        self.code += f"</{self.tagType}>"


