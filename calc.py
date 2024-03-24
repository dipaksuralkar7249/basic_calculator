import tkinter as tk
root  = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

en = tk.Label(root,bg="lightgrey",fg="blue",font="Arial 30",width=300,height=1)
en.pack()

b1 = tk.Button(root,text="1",font="Arial 30").place(x= 10,y = 60)
b2 = tk.Button(root,text="2",font="Arial 30").place(x = 80, y = 60)
b3 = tk.Button(root,text="3",font="Arial 30").place(x = 150,y = 60)
b4 = tk.Button(root,text="C",font="Arial 30 bold", fg="black", bg = "blue").place(x = 220,y = 60)
#b5 = tk.Button(root,text="5",font="Arial 25").place(row = 3,column = 1)
#b6 = tk.Button(root,text="6",font="Arial 25").place(row = 3,column = 2)
#b7 = tk.Button(root,text="7",font="Arial 25").place(row = 4,column = 0)
#b8 = tk.Button(root,text="8",font="Arial 25").place(row = 4,column = 1)
#b9 = tk.Button(root,text="9",font="Arial 25").place(row = 4,column = 2)
#b0 = tk.Button(root,text="0",font="Arial 25").grid(row = 4, column = 0 ,padx = 10)






root.mainloop()