from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title("clock")
def time():
	string=strftime('%H:%M:%S %P')
	label.config(text=string)
	label.after(100,time)
label=Label(root,font=("DS-DIGIT.TTF.",40),background="black",foreground="cyan")
label.pack(anchor='center')
time()
mainloop()