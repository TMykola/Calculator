from interface import *


class Calc():
    def __init__(self):
        self.point = 0
        self.action = False
        self.actions = ["+","-","*","/"]

calc = Calc()

def clicked_1():
    if result.text() != "0":
        result.setText(result.text() + "1")
    else:
        result.setText("1")
def clicked_2():
    if result.text() != "0":
        result.setText(result.text() + "2")
    else:
        result.setText("2")
def clicked_3():
    if result.text() != "0":
        result.setText(result.text() + "3")
    else:
        result.setText("3")
def clicked_4():
    if result.text() != "0":
        result.setText(result.text() + "4")
    else:
        result.setText("4")
def clicked_5():
    if result.text() != "0":
        result.setText(result.text() + "5")
    else:
        result.setText("5")
def clicked_6():
    if result.text() != "0":
        result.setText(result.text() + "6")
    else:
        result.setText("6")
def clicked_7():
    if result.text() != "0":
        result.setText(result.text() + "7")
    else:
        result.setText("7")
def clicked_8():
    if result.text() != "0":
        result.setText(result.text() + "8")
    else:
        result.setText("8")
def clicked_9():
    if result.text() != "0":
        result.setText(result.text() + "9")
    else:
        result.setText("9")

def clicked_plus():
    if calc.action and result.text()[-1] in calc.actions:
        result.setText(result.text()[:-1] + "+")
    else:
        if calc.action:
            #clicked_equals()
            pass
        if result.text()[-1] == ".":
            result.setText(result.text()[:-1])
        result.setText(result.text() + "+")
        calc.action = True
        calc.point = 1
      
def clicked_minus():
    if calc.action and result.text()[-1] in calc.actions:
        result.setText(result.text()[:-1] + "-")
    else:
        if calc.action:
            #clicked_equals()
            pass
        if result.text()[-1] == ".":
            result.setText(result.text()[:-1])
        result.setText(result.text() + "-")
        calc.action = True
        calc.point = 1

def clicked_point():
    if not calc.action and calc.point == 0:
        result.setText(result.text() + ".")
        calc.point = 1
    elif calc.action and calc.point == 1:
        if result.text()[-1] in calc.actions:
            result.setText(result.text() + "0.")
        else:
            result.setText(result.text() + ".")
        calc.point = 2
        
def clicked_clear():
    calc.action = False
    result.setText("0")

def clicked_backspace():
    if result.text() != "0":
        result.setText(result.text()[:-1])
    else:
        pass

b_plus.clicked.connect(clicked_plus)
b_minus.clicked.connect(clicked_minus)
b_point.clicked.connect(clicked_point)
b_clear.clicked.connect(clicked_clear)
b_bacspace.clicked.connect(clicked_backspace)
b1.clicked.connect(clicked_1)
b2.clicked.connect(clicked_2)
b3.clicked.connect(clicked_3)
b4.clicked.connect(clicked_4)
b5.clicked.connect(clicked_5)
b6.clicked.connect(clicked_6)
b7.clicked.connect(clicked_7)
b8.clicked.connect(clicked_8)
b9.clicked.connect(clicked_9)


app.exec_()
