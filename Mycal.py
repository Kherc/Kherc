# ===================Imports==================

from guizero import *
import math

# =================Definitions=================

firstlineshow = []
historylist = []


def addnum0():
    firstlineshow.append(0)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum1():
    firstlineshow.append(1)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum2():
    firstlineshow.append(2)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum3():
    firstlineshow.append(3)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum4():
    firstlineshow.append(4)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum5():
    firstlineshow.append(5)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum6():
    firstlineshow.append(6)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum7():
    firstlineshow.append(7)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum8():
    firstlineshow.append(8)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def addnum9():
    firstlineshow.append(9)
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def dot():
    firstlineshow.append(".")
    firstlineshow1 = str(''.join(map(str, firstlineshow)))
    line1.value = firstlineshow1


def plusc():
    if len(historylist) == 0:
        firstlineshowstr = str(''.join(map(str, line1.value)))
        historylist.append(firstlineshowstr)
        historylist.append("+")
        history.value = historylist
        firstlineshow.clear()

    elif len(historylist) == 2:
        result = float(historylist[0]) + float(line1.value)
        result1 = str(result)
        historylist[1] = "+"
        del historylist[0]
        historylist.insert(0, result1)
        history.value = historylist
        firstlineshow.clear()


def minusc():
    if len(historylist) == 0:
        firstlineshowstr = str(''.join(map(str, line1.value)))
        historylist.append(firstlineshowstr)
        historylist.append("-")
        history.value = historylist
        firstlineshow.clear()
    elif len(historylist) == 2:
        result = float(historylist[0]) - float(line1.value)
        historylist[1] = "-"
        del historylist[0]
        historylist.insert(0, result)
        history.value = historylist
        firstlineshow.clear()


def multiplyc():
    if len(historylist) == 0:
        firstlineshowstr = str(''.join(map(str, line1.value)))
        historylist.append(firstlineshowstr)
        historylist.append("x")
        history.value = historylist
        firstlineshow.clear()
    elif len(historylist) == 2:
        result = float(historylist[0]) * float(line1.value)
        historylist[1] = "x"
        del historylist[0]
        historylist.insert(0, result)
        history.value = historylist
        firstlineshow.clear()


def dividec():
    if len(historylist) == 0:
        firstlineshowstr = str(''.join(map(str, line1.value)))
        historylist.append(firstlineshowstr)
        historylist.append("÷")
        history.value = historylist
        firstlineshow.clear()
    elif len(historylist) == 2:
        result = float(historylist[0]) / float(line1.value)
        historylist[1] = "÷"
        del historylist[0]
        historylist.insert(0, result)
        history.value = historylist
        firstlineshow.clear()


def percentc():
    if len(historylist) == 0:
        firstlineshowstr = str(''.join(map(str, line1.value)))
        historylist.append(firstlineshowstr)
        historylist.append("%")
        history.value = historylist
        firstlineshow.clear()
    elif len(historylist) == 2:
        result = (float(historylist[0]) * float(line1.value)) / 100
        historylist[1] = "%"
        del historylist[0]
        historylist.insert(0, result)
        history.value = historylist
        firstlineshow.clear()


def squarerootc():
    if len(historylist) == 0:
        firstlineshowstr = float(''.join(map(str, line1.value)))
        historylist.append("(")
        historylist.append("√")
        historylist.append(firstlineshowstr)
        historylist.append(")")
        history.value = historylist
        result1 = math.sqrt(float(firstlineshowstr))
        line1.value = result1
        firstlineshow.clear()
        historylist.clear()


def squarec():
    if len(historylist) == 0:
        firstlineshowstr = float(''.join(map(str, line1.value)))
        historylist.append("sqr")
        historylist.append("(")
        historylist.append(firstlineshowstr)
        historylist.append(")")
        history.value = historylist
        result1 = float(firstlineshowstr) ** 2
        line1.value = result1
        firstlineshow.clear()
        historylist.clear()


def backspacec():
    newb = line1.value[:-1]
    line1.value = newb
    firstlineshow.clear()
    firstlineshow.append(line1.value)


def clearec():
    firstlineshow.clear()
    line1.value = firstlineshow


def clearc():
    firstlineshow.clear()
    historylist.clear()
    line1.value = firstlineshow
    history.value = historylist


def equalc():
    if historylist[1] == "+":
        result = float(historylist[0]) + float(line1.value)
        historylist.append(line1.value)
        historylist.append("=")
        history.value = historylist
        line1.value = result
        firstlineshow.clear()
        historylist.clear()
    elif historylist[1] == "-":
        result = float(historylist[0]) - float(line1.value)
        historylist.append(line1.value)
        historylist.append("=")
        history.value = historylist
        line1.value = result
        firstlineshow.clear()
        historylist.clear()
    elif historylist[1] == "x":
        result = float(historylist[0]) * float(line1.value)
        historylist.append(line1.value)
        historylist.append("*")
        history.value = historylist
        line1.value = result
        firstlineshow.clear()
        historylist.clear()
    elif historylist[1] == "÷":
        result = float(historylist[0]) / float(line1.value)
        historylist.append(line1.value)
        historylist.append("=")
        history.value = historylist
        line1.value = result
        firstlineshow.clear()
        historylist.clear()
    elif historylist[1] == "%":
        result = float(historylist[0]) * float(line1.value) / 100
        historylist.append(line1.value)
        historylist.append("=")
        history.value = historylist
        line1.value = result
        firstlineshow.clear()
        historylist.clear()


def negposc():
    negativeorpositive = -(float(line1.value))
    line1.value = negativeorpositive
    firstlineshow.clear()
    firstlineshow.append(line1.value)
# =======GUIZero stuff=========
# -----------------------------
# ========Boxes and the app =========


cal = App(title="Calculator", height=311, width=196, bg="white", layout="grid")
mainbox = Box(cal, layout="grid", grid=[0, 0])
resultsbox = Box(mainbox, layout="grid", grid=[0, 0])
buttonsbox = Box(mainbox, layout="grid", grid=[0, 1])
# =====Resultboxes===========
history = Text(resultsbox, text="", grid=[0, 0])
line1 = Text(resultsbox, text="", grid=[0, 1])
# ===========Buttons=========
bakcspace = PushButton(buttonsbox, text="⌫", width=3, height=1, command=backspacec, grid=[3, 0])
clear = PushButton(buttonsbox, text="C", width=3, height=1, command=clearc, grid=[2, 0])
cebutt = PushButton(buttonsbox, text="CE", width=3, height=1, command=clearec, grid=[1, 0])
percent = PushButton(buttonsbox, text="%", width=3, height=1, command=percentc, grid=[0, 0])
# ----Second row-----
negandpos = PushButton(buttonsbox, text="+/-", width=3, height=1, command=negposc, grid=[3, 1])
squareroot = PushButton(buttonsbox, text="√", width=3, height=1, command=squarerootc, grid=[2, 1])
square = PushButton(buttonsbox, text=" x²", width=3, height=1, command=squarec, grid=[1, 1])
divide = PushButton(buttonsbox, text="÷", width=3, height=1, command=dividec, grid=[0, 1])
# ----Third row-----
multiply = PushButton(buttonsbox, text="x", width=3, height=1, command=multiplyc, grid=[3, 2])
nine = PushButton(buttonsbox, text="9", width=3, height=1, command=addnum9, grid=[2, 2])
eight = PushButton(buttonsbox, text="8", width=3, height=1, command=addnum8, grid=[1, 2])
seven = PushButton(buttonsbox, text="7", width=3, height=1, command=addnum7, grid=[0, 2])
# ----Fourth row-----
minus = PushButton(buttonsbox, text="-", width=3, height=1, command=minusc, grid=[3, 3])
six = PushButton(buttonsbox, text="6", width=3, height=1, command=addnum6, grid=[2, 3])
five = PushButton(buttonsbox, text="5", width=3, height=1, command=addnum5, grid=[1, 3])
four = PushButton(buttonsbox, text="4", width=3, height=1, command=addnum4, grid=[0, 3])
# ----Fifth row----
plus = PushButton(buttonsbox, text="+", width=3, height=1, command=plusc, grid=[3, 4])
three = PushButton(buttonsbox, text="3", width=3, height=1, command=addnum3, grid=[2, 4])
two = PushButton(buttonsbox, text="2", width=3, height=1, command=addnum2, grid=[1, 4])
one = PushButton(buttonsbox, text="1", width=3, height=1, command=addnum1, grid=[0, 4])
# ----Sixth row----
equal = PushButton(buttonsbox, text="=", width=3, height=1, command=equalc, grid=[3, 5])
pofloat = PushButton(buttonsbox, text=".", width=3, height=1, command=dot, grid=[2, 5])
zero = PushButton(buttonsbox, text="0", width=3, height=1, command=addnum0, grid=[1, 5])
caal = Text(buttonsbox, size=24, text="🪐", grid=[0, 5])
cal.display()
