
#First Screen
from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import time

root = Tk()

# image view
height = 650
width = 600
#The x and y variables are used to calculate the position of the window on the screen
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)

root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#remove the window frame and title bar from the root window. This makes the window appear as a floating window without any borders or decorations.
root.overrideredirect(1)
#The '-topmost' attribute is a Tkinter attribute that can be used to control the stacking order of windows.
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')
#background image
image=PhotoImage(file="IMS LOGO.png")
bg_label = Label(root, i=image)
bg_label.place(x=0, y=0)



progress_label = Label(root, text="Please Wait...", font=('arial', 13, 'bold'), fg='black')
progress_label.place(x=225, y=450)
progress = Progressbar(root, orient=HORIZONTAL, length=550, mode='determinate')
progress.place(x=25, y=500)



exit_btn = Button(text='x', bg='red', command=lambda: exit_window(), bd=0, font=("arial", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=570, y=0)
def exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    os.system("python main.py")
    root.destroy() 
i = 0

def loadsystem():




    
    global i
    if i <= 100:
        if i>50 & i<60:
            time.sleep(0.1)
        
        txt = 'Please Wait...  ' + (str(i)+'%')
        progress_label.config(text=txt)
        progress_label.after(10, loadsystem)
        progress['value'] = i
        i += 1
    else:
        top()

loadsystem()
root.mainloop()

