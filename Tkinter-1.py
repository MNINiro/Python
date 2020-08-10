##The size of any master widget is determined by the size of the “slave widgets” inside.
##The packer is used to control where slave widgets appear inside the master into which
##they are packed. You can pack widgets into frames, and frames into other frames,
##in order to achieve the kind of layout you desire. Additionally, the arrangement
##is dynamically adjusted to accommodate incremental changes to the configuration,
##once it is packed.

##from tkinter import *
##
##class Window(Frame):
##    def __init__(self, master=None):
##        Frame.__init__(self, master)
##        self.master = master
##
### initialize tkinter
##root = Tk()
##app = Window(root)
##
### set window title
##root.wm_title("Tkinter window")
##
### show window
##root.mainloop()

#==============================


import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top") # The pack() method can be called with
                                       # keyword-option/value pairs that control where
                                       # the widget is to appear within its container,
                                       # and how it is to behave when the main application
                            # window is resized.Values are: 'left', 'right', 'top', 'bottom'.

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)# Close the form (container)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()


#================================


##class App(tk.Frame):
##    def __init__(self, master=None):
##        super().__init__(master)
##        self.pack()
##
### create the application
##myapp = App()
##
###
### here are method calls to the window manager class
###
##myapp.master.title("My Do-Nothing Application")
##myapp.master.maxsize(1000, 400)
##
### start the program
##myapp.mainloop()
