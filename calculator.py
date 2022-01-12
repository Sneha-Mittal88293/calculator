from tkinter import *
root = Tk()
root.title('sneha calculator')
#root.geometry('400x400')
e1 = Entry(root,width = 16,justify="right",font = "arial 25",bd = 7,bg = "cadetblue")
e1.grid(row =0,column = 0,columnspan =4)

def calc(d):
    e1.insert(16,d)

def result(r):
    e1.delete(0,END)
    e1.insert(16,r)
    
def clear(e):
    e1.delete(0,END)
    

b1 = Button(root,text = '7',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("7")).grid(row=1,column=0)
b2 = Button(root,text = '8',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("8")).grid(row=1,column=1)
b3 = Button(root,text = '9',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("9")).grid(row=1,column=2)
b4 = Button(root,text = 'c',width =5 , height = 2,font = "arial 16",bd = 4,command=lambda:clear(e1.get())).grid(row=1,column=3)
b5 = Button(root,text = '4',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("4")).grid(row=2,column=0)
b6 = Button(root,text = '5',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("5")).grid(row=2,column=1)
b7 = Button(root,text = '6',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("6")).grid(row=2,column=2)
b8 = Button(root,text = '*',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("*")).grid(row=2,column=3)
b9 = Button(root,text = '1',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("1")).grid(row=3,column=0)
b10 = Button(root,text = '2',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("2")).grid(row=3,column=1)
b11 = Button(root,text = '3',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("3")).grid(row=3,column=2)
b12 = Button(root,text = '+',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("+")).grid(row=3,column=3)
b13 = Button(root,text = '0',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("0")).grid(row=4,column=0)
b14 = Button(root,text = '.',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc(".")).grid(row=4,column=1)
b15 = Button(root,text = '-',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:calc("-")).grid(row=4,column=2)
b16 = Button(root,text = '=',width = 5 , height = 2,font = "arial 16",bd = 4,command=lambda:result(eval(e1.get()))).grid(row=4,column=3)