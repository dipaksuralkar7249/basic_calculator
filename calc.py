import tkinter as tk
root  = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x430")

en = tk.Entry(root,bg="lightgrey",fg="black",font="Arial 30",width=300)
en.pack()

def addnum(num):
    if num == 1:
        en.insert(0,1)
    elif num == 2:
        en.insert(0,2)
    elif num == 3:
        en.insert(0,3)
    elif num == 4:
        en.insert(0,4)
    elif num == 5:
        en.insert(0,5)
    elif num == 6:
        en.insert(0,6)
    elif num == 7:
        en.insert(0,7)
    elif num == 8:
        en.insert(0,8)
    elif num == 9:
        en.insert(0,9)
    elif num == 0:
        en.insert(0,0)

def cancelnum():
    en.delete(0,tk.END)

b1 = tk.Button(root,text="1",font="Arial 30",command=lambda :addnum(1)).place(x= 10,y = 60)
b2 = tk.Button(root,text="2",font="Arial 30",command=lambda :addnum(2)).place(x = 80, y = 60)
b3 = tk.Button(root,text="3",font="Arial 30",command=lambda :addnum(3)).place(x = 150,y = 60)        #FIRST ROW
bc = tk.Button(root,text="C",font="Arial 30 ", fg="black", bg = "#03cafc", command=cancelnum).place(x = 220,y = 60)

b4 = tk.Button(root,text="4",font="Arial 30",command=lambda :addnum(4)).place(x = 10,y = 150)
b5 = tk.Button(root,text="5",font="Arial 30", command=lambda :addnum(5)).place(x = 80,y = 150)
b6 = tk.Button(root,text="6",font="Arial 30", command=lambda :addnum(6)).place(x = 150,y = 150)         #SECOND ROW
bplus = tk.Button(root,text="+",font="Arial 30 bold",bg ="#03cafc", command=lambda :addnum("+")).place(x = 220,y = 150)

b7 = tk.Button(root,text="7",font="Arial 30", command=lambda :addnum(7)).place(x = 10,y = 240)
b8 = tk.Button(root,text="8",font="Arial 30", command=lambda :addnum(8)).place(x = 80,y = 240)
b9 = tk.Button(root,text="9",font="Arial 30",command=lambda :addnum(9)).place(x = 150,y = 240)    #THIRD ROW
bsub = tk.Button(root,text="-",font="Arial 31 bold", bg="#03cafc", command=lambda :addnum("-")).place(x = 220,y = 240)

zero = tk.Button (root, text="0",font = "Arial 31 bold", command=lambda :addnum(0)).place(x =10 , y =330)
mul = tk.Button(root,text = "*",font = "Arial 31 bold", bg ="#03cafc",command=lambda :addnum("*")).place(x = 80,y = 330)
div = tk.Button(root,text="/", font = "Arial 31 bold", bg="#03cafc", command=lambda :addnum("/")).place(x = 150, y = 330)  #fourth row
equal = tk.Button(root,text = "=", font="Arial 31 bold", bg="#03cafc").place(x = 220, y = 330)




root.mainloop()