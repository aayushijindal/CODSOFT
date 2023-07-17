import tkinter as tki

calculation=""

def add(symbol):
    global calculation
    calculation+= str(symbol)
    result.delete(1.0,"end")
    result.insert(1.0,calculation)

def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)
    except:
        clear()
        result.insert(1.0,"Error!")

def clear():
    global calculation
    calculation= ""
    result.delete(1.0,"end")


root=tki.Tk()
root.geometry("495x280")

result=tki.Text(root,height=2,width=27,bg='#98bf64',fg='black',font=("ariel",24))
result.grid(columnspan=5)


btnmrc=tki.Button(root,text="mrc",command=lambda:add("mrc"), width=8,bg='#57595d',fg='black',font=("ariel",15))
btnmrc.grid(row=1,column=1)
# btnmrc.place(x=30,y=130)

btnm1=tki.Button(root,text="m-",command=lambda:add("m-"), width=8,bg='#57595d',fg='black',font=("ariel",15))
btnm1.grid(row=1,column=2)


btnm2=tki.Button(root,text="m+",command=lambda:add("m+"), width=8,bg='#57595d',fg='black',font=("ariel",15))
btnm2.grid(row=1,column=3)

btndiv=tki.Button(root,text="/",command=lambda:add("/"), width=8,bg='#ff4d4d',fg='black',font=("ariel",15))
btndiv.grid(row=1,column=4)


btn7=tki.Button(root,text="7",command=lambda:add(7), width=8,bg='black',fg='white',font=("ariel",15))
btn7.grid(row=2,column=1)
#btn7.place(y=90)

btn8=tki.Button(root,text="8",command=lambda:add(8), width=8,bg='black',fg='white',font=("ariel",15))
btn8.grid(row=2,column=2)

btn9=tki.Button(root,text="9",command=lambda:add(9), width=8,bg='black',fg='white',font=("ariel",15))
btn9.grid(row=2,column=3)

btnmulti=tki.Button(root,text="*",command=lambda:add("*"), width=8,bg='#ff4d4d',fg='black',font=("ariel",15))
btnmulti.grid(row=2,column=4)


btn4=tki.Button(root,text="4",command=lambda:add(4), width=8,bg='black',fg='white',font=("ariel",15))
btn4.grid(row=3,column=1)

btn5=tki.Button(root,text="5",command=lambda:add(5), width=8,bg='black',fg='white',font=("ariel",15))
btn5.grid(row=3,column=2)

btn6=tki.Button(root,text="6",command=lambda:add(6), width=8,bg='black',fg='white',font=("ariel",15))
btn6.grid(row=3,column=3)

btnminus=tki.Button(root,text="-",command=lambda:add("-"), width=8,bg='#ff4d4d',fg='black',font=("ariel",15))
btnminus.grid(row=3,column=4)

btn1=tki.Button(root,text="1",command=lambda:add(1), width=8,bg='black',fg='white',font=("ariel",15))
btn1.grid(row=4,column=1)

btn2=tki.Button(root,text="2",command=lambda:add(2), width=8,bg='black',fg='white',font=("ariel",15))
btn2.grid(row=4,column=2)

btn3=tki.Button(root,text="3",command=lambda:add(3), width=8,bg='black',fg='white',font=("ariel",15))
btn3.grid(row=4,column=3)

btnplus=tki.Button(root,text="+",command=lambda:add("+"), width=8,bg='#ff4d4d',fg='black',font=("ariel",15))
btnplus.grid(row=4,column=4)

btn4=tki.Button(root,text="0",command=lambda:add(0), width=8,bg='black',fg='white',font=("ariel",15))
btn4.grid(row=5,column=1)

btn4=tki.Button(root,text=".",command=lambda:add("."), width=8,bg='black',fg='white',font=("ariel",15))
btn4.grid(row=5,column=2)

btn4=tki.Button(root,text="C",command=clear, width=8,bg='black',fg='white',font=("ariel",15))
btn4.grid(row=5,column=3)

btnequal=tki.Button(root,text="=",command=evaluate, width=8,bg='#d8b863',fg='black',font=("ariel",15))
btnequal.grid(row=5,column=4)


root.mainloop()
