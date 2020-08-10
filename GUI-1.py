##import tkinter as tk
##
##root = tk.Tk()
##
##S = tk.Scrollbar(root)
##T = tk.Text(root, height=4, width=50)
##
##S.pack(side=tk.RIGHT, fill=tk.Y)
##T.pack(side=tk.LEFT, fill=tk.Y)
##
##S.config(command=T.yview)
##T.config(yscrollcommand=S.set)
##
##quote = """HAMLET: To be, or not to be--that is the question:
##Whether 'tis nobler in the mind to suffer
##The slings and arrows of outrageous fortune
##Or to take arms against a sea of troubles
##And by opposing end them. To die, to sleep--
##No more--and by a sleep to say we end
##The heartache, and the thousand natural shocks
##That flesh is heir to. 'Tis a consummation
##Devoutly to be wished."""
##T.insert(tk.END, quote)
##tk.mainloop()

#===============================

import tkinter as tk

root = tk.Tk()

text1 = tk.Text(root, height=20, width=27)

photo = tk.PhotoImage(file='./William_Shakespeare.gif')

text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)
text1.pack(side=tk.RIGHT) # Show the photo at the right side

text2 = tk.Text(root, height=20, width=45)

scroll = tk.Scrollbar(root, command=text2.yview)

text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nWilliam Shakespeare\n', 'big')

quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)

scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
