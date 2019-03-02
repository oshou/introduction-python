class Member:
    LANG = 'JP'

    def __init__(self):
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

taro = Member()
taro.setName("太郎")
print(taro.getName())
print(Member.LANG)
