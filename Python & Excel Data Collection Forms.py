from tkinter import *
import pandas as pd
import tkinter.messagebox

def Exit():
    Exit = tkinter.messagebox.askyesno("Quit from The This Page", "Conform if you want to Quit")
    if Exit > 0:
        master.destroy()
        return
def submit_fields():
    path='Details collect.xlsx'
    df1=pd.read_excel(path)

    SeriesA = df1['Items Name']
    SeriesB = df1['Quantity']
    SeriesC = df1['Price']

    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())

    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)

    df2=pd.DataFrame({'Items Name':SeriesA,'Quantity':SeriesB,'Price':SeriesC})
    df2.to_excel(path,index=False)

    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)

master=Tk()
master.geometry('480x155')
master.resizable(False,False)
master.config(bg='powder blue')

Label(master,text="Items Name",fg='black',font=("arial",12,"bold"),bg='grey',width=15).grid(row=0)
Label(master,text="Quantity",fg='black',font=("arial",12,"bold"),bg='grey',width=15).grid(row=1)
Label(master,text="Price",fg='black',font=("arial",12,"bold"),bg='grey',width=15).grid(row=2)

entry1=Entry(master,bd=5,width=30,font=("Segoe UI Black",12,"bold"))
entry1.grid(row=0,column=1)

entry2=Entry(master,bd=5,width=30,font=("Segoe UI Black",12,"bold"))
entry2.grid(row=1 ,column=1)

entry3=Entry(master,bd=5,width=30,font=("Segoe UI Black",12,"bold"))
entry3.grid(row=2 ,column=1)

Button(master,text="Quit",bg='red',command=Exit).grid(row=3,columnspan=2,pady=4)
Button(master,text="Submit",bg='spring green',command=submit_fields).grid(row=3,column=0,pady=4)
master.mainloop()


