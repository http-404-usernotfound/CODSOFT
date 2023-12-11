from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.properties import ListProperty

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 650)
Config.set('graphics', 'resizable', False)

class Calculator(BoxLayout):
    displayImageList = ListProperty(['../None.png']*10)

    count = 0
    noToImage = {'1':'../One(only).png', '2':'../Two(only).png', '3':'../Three(only).png'
                 , '4':'../Four(only).png', '5':'../Five(only).png', '6':'../Six(only).png'
                 , '7':'../Seven(only).png', '8':'../Eight(only).png', '9':'../Nine(only).png'
                 , '0':'../Zero(only).png', '(':'../OpenB(only).png', ')':'../CloseB(only).png'
                 , '.':'../Dot(only).png', '+':'../Plus(only).png', '-':'../Minus(only).png'
                 , '*':'../Multiply(only).png', '/':'../Divide(only).png', '':'../None.png'}
    expression = ''
    def addChar(self, event,  num):
        self.expression += num
        self.count += 1
        self.updateDisplay()


    def evaluate(self, event):
        if self.expression != '':
            try:
                self.expression = eval(self.expression)
                if not (abs(self.expression - int(self.expression)) > 0):
                    self.expression = int(self.expression)

                self.expression = str(self.expression)
                self.updateDisplay()
                self.count = len(self.expression)
            except SyntaxError:
                self.expression = ''
            except ZeroDivisionError:
                self.expression = ''



    def allClear(self, event):
        self.expression = ''
        self.count = 0
        self.updateDisplay()


    def delete(self, event):
        self.expression = self.expression[0:len(self.expression)-1]
        self.count -= 1
        self.updateDisplay()


    def updateDisplay(self):
        self.expression = self.expression[:10]
        if self.count<=10:
            rev_exp = self.expression[::-1]
            length = 0
            if len(rev_exp) > 10:
                length = 10
            else:
                length = len(rev_exp)

            for i in range(length):
                self.displayImageList[9-i] = self.noToImage[rev_exp[i]]
            i = 9-length
            while i>=0:
                self.displayImageList[i] = self.noToImage['']
                i-=1
            print(self.displayImageList)


class MainApp(App):
    pass

root = MainApp()
root.run()
