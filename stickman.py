
from tkinter import *

root = Tk()
  
C = Canvas(root, bg ="black",
           height = 600, width = 600)
    
C.create_oval(275,250,325,300,fill = "white")
C.create_rectangle(300,250,300,300,fill="cyan")
#C.create_oval(280,250,325,300,fill = "red")
  
C.pack()
root.mainloop()