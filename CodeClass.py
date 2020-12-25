class Code:

    def __init__(self, content,tagStyle="dark",tagType='h1',):
        self.code = f"<{tagType} class='{tagStyle}'>"
        self.code += content
        self.code += f"</{tagType}>"

