import tkinter as tk
root  = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

en = tk.Label(root,bg="lightgrey",fg="blue",font="Arial 30",width=300,height=1)
en.pack()

b1 = tk.Button(root,text="1",font="Arial 30").place(x= 10,y = 60)
b2 = tk.Button(root,text="2",font="Arial 30").place(x = 80, y = 60)
b3 = tk.Button(root,text="3",font="Arial 30").place(x = 150,y = 60)        #FIRST ROW
bc = tk.Button(root,text="C",font="Arial 30 ", fg="black", bg = "#03cafc").place(x = 220,y = 60)

b4 = tk.Button(root,text="5",font="Arial 30").place(x = 10,y = 150)
b5 = tk.Button(root,text="6",font="Arial 30").place(x = 80,y = 150)
b6 = tk.Button(root,text="7",font="Arial 30").place(x = 150,y = 150)         #SECOND ROW
bplus = tk.Button(root,text="+",font="Arial 30 bold",bg ="#03cafc").place(x = 220,y = 150)

b7 = tk.Button(root,text="7",font="Arial 30").place(x = 10,y = 240)
b8 = tk.Button(root,text="8",font="Arial 30").place(x = 80,y = 240)
b9 = tk.Button(root,text="9",font="Arial 30").place(x = 150,y = 240)    #THIRD ROW
bsub = tk.Button(root,text="-",font="Arial 31 bold", bg="#03cafc").place(x = 220,y = 240)




root.mainloop()