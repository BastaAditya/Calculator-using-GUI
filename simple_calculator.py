from tkinter import *
calculator = Tk() #creating window
ans = 0 #initializing answer to 0.

def number(a):
    f1 = show.get()
    show.delete(0, END)#deleting the number before.
    if f1 == "0" or f1 == "+" or f1 == "-" or f1 == "*" or f1 == "/": #if statement to not get the operator in the number and also to remove the zero at the beginning.
        b = a
    else:
        b = f1 + a
    show.insert(0,b) #displaying the new number.

def add():
    global ans 
    ans = float(show.get()) #storing the number entered into the final answer.
    show.delete(0, END)
    show.insert(0,"+")
    global operator
    operator = "+" #assigning operator to the equation.
    

def sub():
    global ans
    ans = float(show.get())
    show.delete(0, END)
    show.insert(0, "-")
    global operator
    operator = "-"

def mul():
    global ans
    ans = float(show.get())
    show.delete(0,END)
    show.insert(0, "*")
    global operator
    operator = "*"

def div():
    global ans
    ans = float(show.get())
    show.delete(0, END)
    show.insert(0, "/")
    global operator
    operator = "/"

def equal():
    global ans
    global operator
    if operator == "+":#checking for the operator and then completing the operation.
        ans = ans + float(show.get())
    if operator == "-":
        ans = ans - float(show.get())
    if operator == "*":
        ans = ans * float(show.get())
    if operator == "/":
        ans = ans / float(show.get())
    show.delete(0, END)
    show.insert(0,ans)
def cl():
    show.delete(0, END)#Clearing the field.

show = Entry(calculator,width = 35, borderwidth =5)
show.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
show.insert(0, "0")
seven = Button(calculator, text = "7", padx = 40, pady = 20, command = lambda : number("7"))#Creating the buttons.
eight = Button(calculator, text = "8", padx = 40, pady = 20, command = lambda : number("8"))
nine = Button(calculator, text = "9", padx = 40, pady = 20, command = lambda : number("9"))
four = Button(calculator, text = "4", padx = 40, pady = 20, command = lambda : number("4"))
five = Button(calculator, text = "5", padx = 40, pady = 20, command = lambda : number("5"))
six = Button(calculator, text = "6", padx = 40, pady = 20, command = lambda : number("6"))
one = Button(calculator, text = "1", padx = 40, pady = 20, command = lambda : number("1"))
two = Button(calculator, text = "2", padx = 40, pady = 20, command = lambda : number("2"))
three = Button(calculator, text = "3", padx = 40, pady = 20, command = lambda : number("3"))
zero = Button(calculator, text = "0", padx = 40, pady = 20, command = lambda : number("0"))

seven.grid(row = 1, column = 0)#Placing the buttons.
eight.grid(row = 1, column = 1)
nine.grid(row = 1, column = 2)
four.grid(row = 2, column = 0)
five.grid(row = 2, column = 1)
six.grid(row = 2, column = 2)
one.grid(row = 3, column = 0)
two.grid(row = 3, column = 1)
three.grid(row = 3, column = 2)
zero.grid(row = 4, column = 0)

plus = Button(calculator, text = "+", padx = 40, pady = 20, command = add)#Creaing operators and other buttons.
minus = Button(calculator, text = "-", padx = 40, pady = 20, command = sub)
multiply = Button(calculator, text = "*", padx = 40, pady = 20, command = mul)
divide = Button(calculator, text = "/", padx = 40, pady = 20, command = div)
clear = Button(calculator, text = "Clear", padx = 30, pady = 20, command = cl)
equal = Button(calculator, text = "=", padx = 140, pady = 20, command = equal)

plus.grid(row = 4, column = 1)#Placing buttons.
minus.grid(row = 4, column = 2)
multiply.grid(row = 5, column = 0)
divide.grid(row = 5, column = 1)
clear.grid(row = 5, column = 2)
equal.grid(row = 6, column = 0, columnspan = 3)
