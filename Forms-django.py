from tkinter import *
##
##
##window = Tk() 
##window.title("Welcome to LikeGeeks app") 
##window.geometry('350x200')
##
##
##lbl = Label(window, text="Hello") 
##lbl.grid(column=0, row=0)
##
##txt = Entry(window,width=10)#it will create a text box to enter data
##txt.grid(column=1, row=0)
##txt.focus() # put the cursor in the text box
####txt = Entry(window,width=10, state='disabled') # To disable entry widget,
##                                                 # you can set the state property to disabled
##
##def clicked():
####    lbl.configure(text="Button was clicked !!") 
##
##    res = "Welcome to " + txt.get()
##    lbl.configure(text= res)
##    
##
##btn = Button(window, text="Click Me", bg="black", fg="white", command = clicked) 
##btn.grid(column=2, row=0)
##
##
##window.mainloop()

#============== Combo Box ===================================

##from tkinter.ttk import *
##
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
## 
##combo = Combobox(window)
##combo['values']= (1, 2, 3, 4, 5, "Text")
##combo.current(3) #set the selected item
##combo.grid(column=0, row=0)
## 
##window.mainloop()


#============= Check Box ====================================

 
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
## 
##chk_state = BooleanVar()
##
##chk_state.set(True) #set check state
##chk = Checkbutton(window, text='Choose', var=chk_state)
##chk.grid(column=0, row=0)
##
####chk_state = IntVar()
##
####chk_state.set(0) #uncheck
####chk_state.set(1) #check
## 
##window.mainloop()


#============= Radio Button ====================================


##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
##
##selected = IntVar()
##
##rad1 = Radiobutton(window,text='First', value=1, variable=selected)
##rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
##rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
## 
##def clicked():
##   print(selected.get())
## 
##btn = Button(window, text="Click Me", command=clicked)
## 
##rad1.grid(column=0, row=0)
##rad2.grid(column=1, row=0)
##rad3.grid(column=2, row=0)
##
##btn.grid(column=3, row=0)
## 
##window.mainloop()




#=============== Scroll Bar ==================================


##from tkinter import *
##from tkinter import scrolledtext
## 
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('450x200')
## 
##txt = scrolledtext.ScrolledText(window,width=40,height=10)
##txt.grid(column=0,row=0)
##
##txt.insert(INSERT,'You text goes here')
##
##def clicked():
##   txt.delete(1.0,END)
## 
##btn = Button(window, text="Clear Text", command=clicked)
##    
##btn.grid(column=3, row=0)
##
##window.mainloop()



#================ Message box =================================

##from tkinter import messagebox
## 
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
## 
##def clicked():
##    messagebox.showinfo('Message title', 'Message content')     #show info 
##    messagebox.showwarning('Message title', 'Message content')  #shows warning message
##    messagebox.showerror('Message title', 'Message content')    #shows error message
##
##
##def diffClicked():
##    res = messagebox.askquestion('Message title','Message content')
##    res = messagebox.askyesno('Message title','Message content')
##    res = messagebox.askyesnocancel('Message title','Message content')
##    res = messagebox.askokcancel('Message title','Message content')
##    res = messagebox.askretrycancel('Message title','Message content')
##
##
####def close_button():
####    exit
####          
##
##
##btn = Button(window,text='Message Type', command=clicked)
##btn.grid(column=0,row=0)
##
##
##btn1 = Button(window,text='Message True/False', command=diffClicked)
##btn1.grid(column=2,row=0)
##
##    
####btn2 = Button(window,text='Quit', command = close_button)
####btn2.grid(column=2,row=1)
## 
##window.mainloop()

#=============== Spin Box ==================================

##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
##
##lbl = Label(window, text="From 0 to 100") 
##lbl.grid(column=0, row=0) 
##
##spin = Spinbox(window, from_=0, to=100, width=10)
##spin.grid(column=2,row=0)
##
##lbl1 = Label(window, text="From 3 to 11") 
##lbl1.grid(column=0, row=2)
##         
##spin1 = Spinbox(window, values=(3, 8, 11), width=10) #You can specify the numbers for the 
##spin1.grid(column=2,row=2)                          #Spinbox instead of using the whole range
##
##
##def defaultValue(var):
##    var =IntVar()
##    var.set(36)
##    spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
##
##btn = Button(window,text='Default Value', command=defaultValue(0))
##btn.grid(column=4,row=0)
##
##window.mainloop()


#============= Progress bar ================================

##from tkinter import *
##from tkinter.ttk import Progressbar
##from tkinter import ttk
## 
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('350x200')
## 
##style = ttk.Style()
##style.theme_use('default')
##style.configure("black.Horizontal.TProgressbar", background='black')
## 
##bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
##bar['value'] = 70
##bar.grid(column=0, row=0)
## 
##window.mainloop()




#================= Menu ============================

from tkinter import *
from tkinter import Menu
from tkinter import messagebox


def new():
    print("You have chosen to create a new file")
    messagebox.showinfo('Message', 'New file has been created')     
 
def edit():
    print("You have chosen to edit existing file")
    messagebox.showinfo('Message', 'File has been edited')   

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('450x200')

menu = Menu(window)

 
File_item = Menu(menu)
File_item.add_command(label='New', command=new)
File_item.add_separator()
File_item.add_command(label='Edit', command = edit )
File_item.add_separator()
File_item.add_command(label="Exit", command=window.destroy)

view_item = Menu(menu)
view_item.add_command(label='Orientation')
view_item.add_separator()
view_item.add_command(label='Format')
 
menu.add_cascade(label='File', menu=File_item)
menu.add_cascade(label='View', menu=view_item)
 
window.config(menu=menu)
 
window.mainloop()

#================= Menu using class ====================

##import tkinter
##import tkinter.scrolledtext as scrolledtext
##
##class GUI(object):
##
##    def __init__(self):
##        root = self.root = tkinter.Tk()
##        root.title('Test')
##
##    # make the top right close button minimize (iconify) the main window
##        root.protocol("WM_DELETE_WINDOW", root.iconify)
##
##    # make Esc exit the program
##        root.bind('<Escape>', lambda e: root.destroy())
##
##    # create a menu bar with an Exit command
##        menubar = tkinter.Menu(root)
##        filemenu = tkinter.Menu(menubar, tearoff=0)
##        filemenu.add_command(label="Exit", command=root.destroy)
##        menubar.add_cascade(label="File", menu=filemenu)
##        root.config(menu=menubar)
##
##    # create a Text widget with a Scrollbar attached
##        txt = scrolledtext.ScrolledText(root, undo=True)
##        txt['font'] = ('consolas', '12')
##        txt.pack(expand=True, fill='both')
##
##gui = GUI()
##gui.root.mainloop()


#================= Tab Control ========================

##from tkinter import *
##from tkinter import ttk
## 
##window = Tk()
##window.title("Welcome to LikeGeeks app")
##window.geometry('450x200')
## 
##tab_control = ttk.Notebook(window)
##
##tab1 = ttk.Frame(tab_control)
##tab2 = ttk.Frame(tab_control)
## 
##tab_control.add(tab1, text='First')
##tab_control.add(tab2, text='Second')
## 
####lbl1 = Label(tab1, text= 'label1')
##lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
##lbl1.grid(column=0, row=0)
## 
##lbl2 = Label(tab2, text= 'label2',padx=5, pady=5)
##lbl2.grid(column=0, row=0)
## 
##tab_control.pack(expand=1, fill='both')
## 
##window.mainloop()

















