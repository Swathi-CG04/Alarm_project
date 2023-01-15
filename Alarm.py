#!/usr/bin/env python
import sys
#import os
from datetime import datetime;
import webbrowser
import click
#import urllib.request

@click.command()
@click.option('-t', '--time', required=True, help='enter the time to set an alarm in HH:MM:SS:AM/PM format')

def main(time):
    #set an alarm
    alarm_time = sys.argv[2]
    validate_time(alarm_time)
    alarm(alarm_time)

def validate_time(alarm_time):
    print("In validation")
    if len(alarm_time) != 11:
        return "Enter the time in valid format"
    elif int(alarm_time[0:2]) > 12:
        return "Enter valid HOUR"
    elif int(alarm_time[3:5]) > 59:
        return "Enter valid MINUTE"
    elif int(alarm_time[6:8]) > 59:
        return "Enter valid SECONDS"
    # elif (alarm_time[9:11]) != ('AM' or 'PM'):
    #     return 'please enter AM / PM'
    else:
        return f'Your Alarm has been set to ${alarm_time}'

def alarm(alarm_time):
    #breaking the alarm time
    #A_HH => Alarm hour
    #C_HH => Current hour
    print("in Alarm")
    A_HH = alarm_time[0:2]
    A_MM = alarm_time[3:5]
    A_SS = alarm_time[6:8]
    A_PE = alarm_time[9:].upper()

    #breaking the current timr
    
#check alaram time with current time   
    while True:
        now = datetime.now()
        C_HH = now.strftime("%I")
        C_MM = now.strftime("%M")
        C_SS = now.strftime("%S")
        C_PE = now.strftime("%p")
        if A_HH == C_HH:
            if A_MM == C_MM:
                if A_SS == C_SS:
                    if A_PE == C_PE:
                        #call play alarm
                        play_alarm()
                        break

#play song in web browser
def play_alarm():
    print("In play Alram")
    strURL='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    ''''with urllib.request.urlopen('https://www.youtube.com/watch?v=dQw4w9WgXcQ') as url:
        s=url.read()
        print(s)'''
    webbrowser.open(strURL, new=2)



#calling main function
if __name__ == "__main__":
    main()
