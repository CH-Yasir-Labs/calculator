#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     01/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

def btn_press(num):
    global equation_text
    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
 try:
    global equation_text
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text=total

 except ZeroDivisionError:
     equation_label.set("Airthmetic Error")
     equation_text=""

 except SyntaxError:
     equation_label.set("Syntax Error")
     equation_text=""


def clear():
     global equation_text
     equation_label.set("")
     equation_text=""

window=Tk()
window.title("Calclator Program")
window.geometry("500x500")

equation_text=""

equation_label=StringVar()

lbl = Label(window, textvariable=equation_label,font=("Times New Roman",20),bg="Yellow",width=24,height=2)
lbl.pack()

frame=Frame(window)
frame.pack()

btn1=Button(frame,text="1",height=4 ,width=9, font=35,command=lambda:btn_press(1))
btn1.grid(row=0,column=0)

btn2=Button(frame,text="2",height=4 ,width=9, font=35,command=lambda:btn_press(2))
btn2.grid(row=0,column=1)

btn3=Button(frame,text="3",height=4 ,width=9, font=35,command=lambda:btn_press(3))
btn3.grid(row=0,column=2)

btn4=Button(frame,text="4",height=4 ,width=9, font=35,command=lambda:btn_press(4))
btn4.grid(row=1,column=0)

btn5=Button(frame,text="5",height=4 ,width=9, font=35,command=lambda:btn_press(5))
btn5.grid(row=1,column=1)

btn6=Button(frame,text="6",height=4 ,width=9, font=35,command=lambda:btn_press(6))
btn6.grid(row=1,column=2)

btn7=Button(frame,text="7",height=4 ,width=9, font=35,command=lambda:btn_press(7))
btn7.grid(row=2,column=0)

btn8=Button(frame,text="8",height=4 ,width=9, font=35,command=lambda:btn_press(8))
btn8.grid(row=2,column=1)

btn9=Button(frame,text="9",height=4 ,width=9, font=35,command=lambda:btn_press(9))
btn9.grid(row=2,column=2)

btn0=Button(frame,text="0",height=4 ,width=9, font=35,command=lambda:btn_press(0))
btn0.grid(row=3,column=0)

plus=Button(frame,text="➕",height=4 ,width=9, font=35,command=lambda:btn_press('+'))
plus.grid(row=0,column=3)


minus=Button(frame,text="➖",height=4 ,width=9, font=35,command=lambda:btn_press('-'))
minus.grid(row=1,column=3)

multiply=Button(frame,text="❌",height=4 ,width=9, font=35,command=lambda:btn_press('*'))
multiply.grid(row=2,column=3)

divide=Button(frame,text="➗",height=4 ,width=9, font=35,command=lambda:btn_press('/'))
divide.grid(row=3,column=3)


equal=Button(frame,text="🟰",height=4 ,width=9, font=35,command=equals)
equal.grid(row=3,column=2)

decimal=Button(frame,text="•",height=4 ,width=9, font=35,command=lambda:btn_press('.'))
decimal.grid(row=3,column=1)

clear=Button(window,text="Clear",height=4 ,width=12, font=35,command= clear)
clear.pack()


window.mainloop()