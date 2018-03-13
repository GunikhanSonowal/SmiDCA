from smidca import smishing_verify
from Tkinter import *
root=Tk()
root.resizable(width=False, height=False)
root.title("SMIDCA DEMO")

label = Label(root, text = "\nWelcome \n SmiDCA Anti-Phishing Tool\n")
label.pack()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print smishing_verify(inputValue)
    
    window = Toplevel(root)
    if smishing_verify(inputValue) == 1:
        
        First = Label(window, bg = "orange",
                  text = "WARNING SMISHING\n SUSPECTED\n",
                  height = 4, width = 21)
        First.pack()
        Second = Label(window, text = "\n This message has been \n identified as forgery, \n intended to trick you into \n disclosing, personal or \n  other information\n **Suggestions** \n Tap the Proceed Button \n if you know the sender \n\n Tap the Go Back button\n to delete the message \n\n Thank you", height = 16, width = 21)
        Second.pack()
        
    else:
        First = Label(window, bg = "green", text = "\nCONGRATULATIONS\n\n GENUINE MESSAGE\n", height = 4, width = 21)
        First.pack()
        Second = Label(window, text = "\n This message has been \n identified as LEGITIMATE, \n You can visit the \n message \n  **Suggestions** \n Tap the Proceed Button \n to access the message \n\n Tap the Go Back button\n to delete the message \n\n Thank you", height = 16, width = 21)
        Second.pack()
    Buttons1(window)

def close_window():
    root.destroy()
    
class Buttons1():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.b3 = Button(self.master, height=2, width=8,
                         text="Go Back",bg = "#CD6155", command=close_window)
        self.b3.pack(side = LEFT)
        self.b2 = Button(self.master, height=2, width=8,
                         text="Proceed", bg = "#F0b27A", command=close_window)
        self.b2.pack(side = LEFT)
        self.frame.pack()
  

    def display3(self):
        print 'hello button3' 


label = Label(root, text = "\n9********* \n Unknown Number\n", width = 21, bg = "orange")
label.pack()


fp = open("spam.txt", "r")
line = fp.read()

#frame=Frame(root, width=300, height=460)
#frame.pack()

textBox=Text(root, bg = "yellow", height=12,
             width=24)
textBox.insert(END, "\n*>"+line)
root.resizable(width=False, height=False)
textBox.pack()

c = Button(root, text="Skip", bg = "#9b59b6", width=8, height=2, command = close_window)
c.pack(side=LEFT)

b=Button(root, height=2, width=8, text="Verify",
         bg = "#D1F2EB", command=lambda: retrieve_input())
b.config()
b.pack(side=LEFT)





mainloop()
