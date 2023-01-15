import tkinter as tk
 
 
def new_window(Win_class):
    global win2
    try:
        if win2.state() == "normal": win2.focus()
    except NameError as e:
        print(e)
        win2 = tk.Toplevel(win)
        Win_class(win2)
 
class Win2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300+500+200")
        self.root["bg"] = "navy"
 
 
win = tk.Tk()
win.geometry("200x200+200+100")
button = tk.Button(win, text="Open new Window")
button['command'] = lambda: new_window(Win2)
button.pack()
text = tk.Text(win, bg='cyan')
text.pack()
win.mainloop()
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )

# Add buttons
button1 = Button(frame1,text="Exit")
button1.pack(pady=20)

button2 = Button( frame1, text = "Start")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Reset")
button3.pack(pady = 20)

# Execute tkinter
root.mainloop()
