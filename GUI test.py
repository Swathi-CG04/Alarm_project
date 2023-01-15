import tkinter as tk
import time

# Top level window
frame = tk.Tk()
frame.title("Alarm Clock")
frame.geometry('400x400')
frame.configure(bg='black')

tk.Label(frame, text="Welcome",fg = "white",bg = "black",font = "Helvetica 30 bold italic").pack()
tk.Label(frame, text = 'To Alarm Clock' , fg = "white",bg = "black",font = "Helvetica 30 bold italic").pack()

tk.Label(frame, text = 'current time :',fg = "white",bg = "black",font = "Helvetica 30 bold italic ").place(x = 450 ,y = 300)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

curr_time =tk.Label(frame, font ='arial 30 bold', text = '', fg = 'white' ,bg ='black')
curr_time.place(x = 720 , y = 300)
clock()

tk.Label(frame, text=" ",fg = "white",bg = "black",font = "Helvetica 10 bold italic").pack()
tk.Label(frame, text="Enter the time alarm has to be set",fg = "white",bg = "black",font = "Helvetica 16 bold italic").pack()
tk.Label(frame, text=" ",fg = "white",bg = "black",font = "Helvetica 1 bold italic").pack()
# Function for getting Input from textbox and printing it at label widget

def printInput():
    alarm_time  = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+alarm_time,fg = "white",bg = "black",font = "Helvetica 16 bold italic")

# TextBox Creation
inputtxt = tk.Text(frame,height = 1,width = 15)
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text = "Set alarm",command = printInput,font = "Helvetica 15 bold italic")
tk.Label(frame, text=" ",bg = "black",font = "Helvetica 8 bold italic").pack()
printButton.place(x=200, y=200)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
