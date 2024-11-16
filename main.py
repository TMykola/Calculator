from interface import *

class Calc():
    def __init__(self):
        self.point = 0
        self.action = False
        self.actions = ["+","-","*","/","^","%"]

calc = Calc()

def clicked_0():
    if result.text() != "0":
        result.setText(result.text() + "0")

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
            clicked_equals()
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
            clicked_equals()
            pass
        if result.text()[-1] == ".":
            result.setText(result.text()[:-1])
        result.setText(result.text() + "-")
        calc.action = True
        calc.point = 1

def clicked_multiply():
    if calc.action and result.text()[-1] in calc.actions:
        result.setText(result.text()[:-1] + "*")
    else:
        if calc.action:
            clicked_equals()
            pass
        if result.text()[-1] == ".":
            result.setText(result.text()[:-1])
        result.setText(result.text() + "*")
        calc.action = True
        calc.point = 1

def clicked_devision():
    if calc.action and result.text()[-1] in calc.actions:
        result.setText(result.text()[:-1] + "/")
    else:
        if calc.action:
            clicked_equals()
            pass
        if result.text()[-1] == ".":
            result.setText(result.text()[:-1])
        result.setText(result.text() + "/")
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
    calc.point = 0
    result.setText("0")

def clicked_backspace():

    if len(result.text()) == 1:
        result.setText("0")
    elif result.text()[-1] == ".":
        calc.point -= 1
        result.setText(result.text()[:-1])
    elif result.text()[-1] in calc.actions:
        calc.action = False
        result.setText(result.text()[:-1])
    else:
        result.setText(result.text()[:-1])
        
def clicked_power():
    if result.text() != "0":
        result.setText(result.text() + "^")
    calc.action = True
    calc.point = 1

def clicked_percent(): 
    if calc.action and result.text()[-1] in calc.actions: 
        result.setText(result.text()[:-1] + "%") 
    else: 
        if calc.action: 
            clicked_equals() 
            pass 
        if result.text()[-1] == ".": 
            result.setText(result.text()[:-1]) 
        result.setText(result.text() + "%") 
        calc.action = True 
        calc.point = 1

def clicked_equals():
    if calc.action:
        index = 0
        for element in result.text():
            if element in calc.actions:
                break 
            index += 1
        if not (len(result.text()) > index + 1):
            result.setText(result.text() + "0")
        first_value = float(result.text()[:index])
        second_value = float(result.text()[index + 1:])
        action = result.text()[index]

        if action == "+":
            result.setText(str(first_value + second_value))

        elif action == "-":
            result.setText(str(first_value - second_value))

        elif action == "*":
            result.setText(str(first_value * second_value)) 

        elif action == "^":
            second_value = int(second_value - 1)
            res = first_value
            for i in range(second_value):
                res = res * first_value
            result.setText(str(res))
            
        elif action == "%": 
            result.setText(str(first_value / 100))

        elif action == "/":
            if second_value == 0:
                result.setText("На 0 не ділиться")
            else:
                result.setText(str(first_value / second_value))

        if result.text()[-2:] == ".0":
            result.setText(result.text()[:-2])

b_power.clicked.connect(clicked_power)
b_percent.clicked.connect(clicked_percent)
b_plus.clicked.connect(clicked_plus)
b0.clicked.connect(clicked_0)
b_multiplu.clicked.connect(clicked_multiply)
b_divine.clicked.connect(clicked_devision)
b_minus.clicked.connect(clicked_minus)
b_point.clicked.connect(clicked_point)
b_clear.clicked.connect(clicked_clear)
b_bacspace.clicked.connect(clicked_backspace)
b_equals.clicked.connect(clicked_equals)
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
