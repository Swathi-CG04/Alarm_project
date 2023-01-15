import tkinter as tk
from tkinter import simpledialog
import sys
from datetime import datetime;
import webbrowser
import click
import random
import urllib.request
       

#taking input
ROOT = tk.Tk()
ROOT.withdraw()
alarm_time = simpledialog.askstring(title="Test",prompt=" Enter the time alarm has to be set")

                   
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

