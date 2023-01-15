import tkinter as tk
from tkinter import simpledialog
import sys
from datetime import datetime;
import webbrowser
import click
import random
import urllib.request
import time
       

frame = tk.Tk()
frame.title("Alarm Clock")
frame.geometry('400x400')
frame.configure(bg='black')
tk.Label(frame, text="Welcome",fg = "white",bg = "black",font = "Helvetica 30 bold italic").pack()
tk.Label(frame, text = 'To Alarm Clock' , fg = "white",bg = "black",font = "Helvetica 30 bold italic").pack()

tk.Label(frame, text = 'current time :',fg = "white",bg = "black",font = "Helvetica 30 bold italic ").place(x = 450 ,y = 300)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time,font="Castellar 40 bold")
    curr_time.after(1000,clock)

curr_time =tk.Label(frame, font ='arial 30 bold', text = '', fg = 'white' ,bg ='black')
curr_time.place(x = 720 , y = 300)
clock()

tk.Label(frame, text=" ",fg = "white",bg = "black",font = "Helvetica 10 bold italic").pack()
tk.Label(frame, text="Enter the time alarm has to be set",fg = "white",bg = "black",font = "Helvetica 16 bold italic").pack()
tk.Label(frame, text=" ",fg = "white",bg = "black",font = "Helvetica 1 bold italic").pack()


# Function for getting Input from textbox and printing it at label widget
def printInput():
    alarm_time=input_time  = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+input_time,fg = "white",bg = "black",font = "Helvetica 16 bold italic")

# TextBox Creation
inputtxt = tk.Text(frame,height = 1,width = 15)
inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,text = "Set alarm",command = printInput,font = "Helvetica 15 bold italic")
tk.Label(frame, text=" ",bg = "black",font = "Helvetica 8 bold italic").pack()
printButton.place(x=200, y=200)
printButton.pack()

#title.withdraw()
#alarm_time = simpledialog.askstring(title="Test",prompt=" Enter the time alarm has to be set",fg = "black",bg = "white",font = "Helvetica 30 bold italic")


# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()


                   
def play_alarm():
    print("PLAYING ALARM")
    strURL = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                     "https://www.youtube.com/watch?v=Ct6BUPvE2sM",
                     "https://www.youtube.com/watch?v=9bZkp7q19f0"]
    URL=random.choice(strURL)
    length=len(strURL)
    rand = random.randint(0,length-1)
    URL = strURL[rand]
    print(URL)
    webbrowser.open(URL, new=2)
    

def break_time(alarm_time):
    #Breaking the alarm time
    A_HH = alarm_time[0:2]
    A_MM = alarm_time[3:5]
    A_SS = alarm_time[6:8]
    A_PE = alarm_time[9:].upper()
    print("ALARM TIME",A_HH,":",A_MM,":",A_SS,":",A_PE)
    
    while True:
        #Breaking the current time 
        C_TIME = datetime.today().strftime("%I:%M:%S:%p")
        C_HH = C_TIME[0:2]
        C_MM = C_TIME[3:5]
        C_SS = C_TIME[6:8]
        C_PE = C_TIME[9:].upper()
        #print("CURRENT TIME",C_HH,":",C_MM,":",C_SS,":",C_PE)
        
        #check alarm time with current time   
        if A_HH == C_HH:
            if A_MM == C_MM:
                if A_SS == C_SS:
                    if A_PE == C_PE:
                        #call play alarm
                        play_alarm()
                        print("CURRENT TIME==ALARM TIME")
                        break


#validating time
def validate_time(alarm_time):
    print("In validation")
    if len(alarm_time) != 11:
        print( "Enter the time in valid format")
    elif int(alarm_time[0:2]) > 12:
        print( "Enter valid HOUR")
    elif int(alarm_time[3:5]) > 59:
        print( "Enter valid MINUTE")
    elif int(alarm_time[6:8]) > 59:
        print( "Enter valid SECONDS")
    else:
            print("The alarm has been set at - ", alarm_time)
            break_time(alarm_time)




validate_time(alarm_time)
frame.mainloop()
