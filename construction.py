# from tkinter import *
import math

def const_triangle(A,B,r,position) :
    mn = B[0]-A[0]
    md = B[1]-A[1]
    C = [0,0]
    D = [0,0]
    if (position == "L") :
        C[1] = B[1] + math.sqrt((r**2 * mn**2)/(md**2+mn**2))
        C[0] = B[0] + math.sqrt((r**2 * md**2)/(md**2+mn**2))
        D[1] = B[1] - math.sqrt((r**2 * mn**2)/(md**2+mn**2))  
        D[0] = B[0] - math.sqrt((r**2 * md**2)/(md**2+mn**2))
    if (position == "R") :
        C[1] = B[1] + math.sqrt((r**2 * mn**2)/(md**2+mn**2))
        C[0] = B[0] - math.sqrt((r**2 * md**2)/(md**2+mn**2))
        D[1] = B[1] - math.sqrt((r**2 * mn**2)/(md**2+mn**2))  
        D[0] = B[0] + math.sqrt((r**2 * md**2)/(md**2+mn**2))
    return [A[0],A[1],C[0],C[1],D[0],D[1]]

# Trail
# root = Tk()
# background = "black"
# C = Canvas(root, bg = background,height = 600, width = 600)
# C.create_polygon(const_triangle([242,342],[272,310],10,"L"),fill="green")
# C.pack()
# root.mainloop()
