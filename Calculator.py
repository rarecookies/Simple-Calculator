import tkinter
from tkinter import *


root= Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

#     click   :
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0 , str(current) + str(number))


# CLEAR anything:
def button_clear():
    e.delete(0 , END)

# ++++++++ add button:
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)


# ------ sub
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)

# *********** multi
def button_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multi"
    f_num = int(first_number)
    e.delete(0, END)

#//////// div
def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)

# ======= equal button :
def button_equal():
    second_number = e.get()
    e.delete(0 , END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math =="multi":
        e.insert(0, f_num * int(second_number))
    elif math =="div":
        e.insert(0, f_num / int(second_number))



e = Entry(root , width=23, font=("arial",30) , borderwidth=0 ,fg="#ffffff", bg="#17161b")
e.pack()

Button(root,text="C" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#3697f5", command = lambda :button_clear()).place(x=10,y=100)
Button(root,text="/" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36" , command = lambda : button_div()).place(x=290,y=100)
Button(root,text="%" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36" ).place(x=150,y=100)
Button(root,text="*" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36" ,command= lambda :button_multi()).place(x=430,y=100)


Button(root,text="7" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(7)).place(x=10,y=200)
Button(root,text="8" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(8)).place(x=150,y=200)
Button(root,text="9" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(9)).place(x=290,y=200)
Button(root,text="-" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36" ,command = lambda :button_sub()).place(x=430,y=200)


Button(root,text="4" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(4)).place(x=10,y=300)
Button(root,text="5" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(5)).place(x=150,y=300)
Button(root,text="6" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(6)).place(x=290,y=300)
Button(root,text="+" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36" , command = lambda:button_add() ).place(x=430,y=300)


Button(root,text="1" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(1)).place(x=10,y=400)
Button(root,text="2" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(2)).place(x=150,y=400)
Button(root,text="3" ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(3)).place(x=290,y=400)
Button(root,text="0" ,width=11 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#2a2d36",command=lambda :button_click(0)).place(x=10,y=500)


Button(root,text="." ,width=5 , height=1 , font=("arial",30,"bold") , bd=1 ,fg="#66de6e" , bg="#2a2d36").place(x=290,y=500)
Button(root,text="=" ,width=5 , height=4 , font=("arial",30,"bold") , bd=1 ,fg="#ffffff" , bg="#fe9037" , command=lambda : button_equal()).place(x=430,y=400)


root.mainloop()