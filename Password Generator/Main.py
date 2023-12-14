from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from random import randint
from kivy.core.clipboard import Clipboard


def randChar():
        return chr(randint(33, 122))


def randSymbol():
    symbols = ['@', '#', '$', '*', '/', '^', '%', '$', '&']
    return symbols[randint(0, 8)]


def randNum():
    nums = ['1', '2', '3', '4', '5', '6', '7' ,'8', '9', '0']
    return nums[randint(0, 9)]

def get5lettWord():
    line = randint(1, 488)
    with open('5 letter words') as f:
        for i in range(line):
            word = f.readline()
            word = word[:5]
        f.close()
    return word


def get3lettWord():
    line = randint(1, 171)
    with open('3 letter words') as f:
        for i in range(line):
            word = f.readline()
            word = word[:3]
        f.close()
    return word


class PasswdGen(BoxLayout):
    password = StringProperty('')
    complexity = ''
    length = 0
    level = ["Easy", "Moderate", "Difficult", "Extreme!"]
    def genPassEasy(self):
        while self.length>0:
            if self.length >= 5:
                self.password += get5lettWord()
                self.length -= 5

            if self.length >= 3:
                self.password += get3lettWord()
                self.length -= 3
            else:
                self.password += randNum()
                self.length -= 1

    def genPassModerate(self):
        while self.length>0:
            if self.length >= 5:
                self.password += get5lettWord()
                self.length -= 5

            if self.length >= 2:
                self.password += randNum()+randNum()
                self.length -= 2

            if self.length >= 3:
                self.password += get3lettWord()
                self.length -= 3
            else:
                self.password += randNum()
                self.length -= 1


    def genPassDifficult(self):
        while self.length > 0:
            if self.length >= 5:
                self.password = get5lettWord()
                self.length -= 5

            if self.length >= 3:
                self.password += randChar()+randSymbol()+randSymbol()
                self.length -= 3

            if self.length >= 3:
                self.password += get3lettWord()
                self.length -= 3

            if self.length >= 1:
                self.password += randChar()
                self.length -= 1

    def genPassExtreme(self):
        for i in range(self.length):
            self.password += randChar()

    def Generate(self, event1, event2):
        self.password = ''
        self.length = int(event2)
        if event1 == 1:
            self.genPassEasy()

        elif event1 == 2:
            self.genPassModerate()

        elif event1 == 3:
            self.genPassDifficult()

        elif event1 == 4:
            self.genPassExtreme()

    def cpy(self):
        Clipboard.copy(self.password)


class MainApp(App):
    pass


root = MainApp()
root.run()
