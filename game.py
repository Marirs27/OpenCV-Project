import msvcrt
import time
from tkinter import *
from construction import *

def draw_stickman(C,coordinates,background,swords="disable_swords") :

    N = coordinates["Nose"]
    LS = coordinates["Left-Shoulder"]
    RS = coordinates["Right-Shoulder"]
    LE = coordinates["Left-Elbow"]
    RE = coordinates["Right-Elbow"]
    LW = coordinates["Left-Wrist"]
    RW = coordinates["Right-Wrist"]
    LH = coordinates["Left-Hip"]
    RH = coordinates["Right-Hip"]
    LK = coordinates["Left-Knee"]
    RK = coordinates["Right-Knee"]
    LA = coordinates["Left-Ankle"]
    RA = coordinates["Right-Ankle"]
    SL = coordinates["Left-Sword"]
    SR = coordinates["Right-Sword"]

    # Horns
    C.create_oval(N[0]-23,N[1]-65,N[0]+23,N[1]-5,fill = "white")
    C.create_oval(N[0]-23,N[1]-75,N[0]+23,N[1]-15,fill = background,outline=background)

    if swords == "enable_swords" :

        # Left Sword
        C.create_polygon([LW[0]+12+SL[0],LW[1]-12+SL[1],LW[0]+17+SL[0],LW[1]-10+SL[1],LW[0]+117+SL[0],LW[1]-80+SL[1],LW[0]+110+SL[0],LW[1]-80+SL[1]],fill="cyan")
        C.create_polygon([LW[0]+12,LW[1]-13,LW[0]+17,LW[1]-9,LW[0]-12,LW[1]+13,LW[0]-17,LW[1]+9],fill="white")

        # Right Sword 357,392
        C.create_polygon([RW[0]-12+SR[0],RW[1]-12+SR[1],RW[0]-17+SR[0],RW[1]-10+SR[1],RW[0]-117+SR[0],RW[1]-80+SR[1],RW[0]-110+SR[0],RW[1]-80+SR[1]],fill="red")
        C.create_polygon([RW[0]-12,RW[1]-13,RW[0]-17,RW[1]-9,RW[0]+12,RW[1]+13,RW[0]+17,RW[1]+9],fill="white")
    
    # Neck
    C.create_polygon(N[0]-4,N[1]+25,N[0]+4,N[1]+25,((LS[0]+RS[0])//2 +1)+4,LS[1],((LS[0]+RS[0])//2 +1)-4,RS[1],fill="white")

    # Head Helmet
    C.create_oval(N[0]-27,N[1]-27,N[0]+27,N[1]+27,fill = "gray")    
    C.create_oval(N[0]-25,N[1]-25,N[0]+25,N[1]+25,fill = "white")
    # Helmet Strip
    C.create_rectangle(N[0]-5,N[1]-25,N[0]+5,N[1]+25,fill="black")

    # Left Hand 
    C.create_polygon(const_triangle([LE[0],LE[1]],[LS[0],LS[1]],10,"L"),fill="white")
    C.create_polygon(const_triangle([LW[0],LW[1]],[LE[0],LE[1]],8,"L"),fill="white")
    # Shoulder Joint
    C.create_oval(LS[0]-12,LS[1]-12,LS[0]+12,LS[1]+12,fill = "white")
    C.create_oval(LS[0]-10,LS[1]-10,LS[0]+10,LS[1]+10,fill = "black")
    # Elbow Joint
    C.create_oval(LE[0]-10,LE[1]-10,LE[0]+10,LE[1]+10,fill = "white")
    C.create_oval(LE[0]-8,LE[1]-8,LE[0]+8,LE[1]+8,fill = "black")
    # Wrist Joint
    C.create_oval(LW[0]-8,LW[1]-8,LW[0]+8,LW[1]+8,fill = "white")
    C.create_oval(LW[0]-6,LW[1]-6,LW[0]+6,LW[1]+6,fill = "black")
    
    # Right Hand 
    C.create_polygon(const_triangle([RE[0],RE[1]],[RS[0],RS[1]],10,"R"),fill="white")
    C.create_polygon(const_triangle([RW[0],RW[1]],[RE[0],RE[1]],8,"R"),fill="white")
    # Shoulder Joint
    C.create_oval(RS[0]-12,RS[1]-12,RS[0]+12,RS[1]+12,fill = "white")
    C.create_oval(RS[0]-10,RS[1]-10,RS[0]+10,RS[1]+10,fill = "black")
    # Elbow Joint
    C.create_oval(RE[0]-10,RE[1]-10,RE[0]+10,RE[1]+10,fill = "white")
    C.create_oval(RE[0]-8,RE[1]-8,RE[0]+8,RE[1]+8,fill = "black")
    # Wrist Joint
    C.create_oval(RW[0]-8,RW[1]-8,RW[0]+8,RW[1]+8,fill = "white")
    C.create_oval(RW[0]-6,RW[1]-6,RW[0]+6,RW[1]+6,fill = "black")

    # Left Leg 
    C.create_polygon(const_triangle([LK[0],LK[1]],[LH[0],LH[1]],12,"L"),fill="white")
    C.create_polygon(const_triangle([LA[0],LA[1]],[LK[0],LK[1]],8,"L"),fill="white")
    # Left Feet
    C.create_polygon([LA[0]-10,LA[1]+2,LA[0]+10,LA[1]+2,LA[0]+15,LA[1]+12,LA[0]-15,LA[1]+12],fill="white")
    # Thigh Joint
    C.create_oval(LH[0]-14,LH[1]-14,LH[0]+14,LH[1]+14,fill = "white")
    C.create_oval(LH[0]-12,LH[1]-12,LH[0]+12,LH[1]+12,fill = "black")
    # Knee Joint
    C.create_oval(LK[0]-10,LK[1]-10,LK[0]+10,LK[1]+10,fill = "white")
    C.create_oval(LK[0]-8,LK[1]-8,LK[0]+8,LK[1]+8,fill = "black")
    # Ankle Joint
    C.create_oval(LA[0]-8,LA[1]-8,LA[0]+8,LA[1]+8,fill = "white")
    C.create_oval(LA[0]-6,LA[1]-6,LA[0]+6,LA[1]+6,fill = "black")

    # Right Leg 
    C.create_polygon(const_triangle([RK[0],RK[1]],[RH[0],RH[1]],12,"R"),fill="white")
    C.create_polygon(const_triangle([RA[0],RA[1]],[RK[0],RK[1]],8,"R"),fill="white")
    # Right Feet
    C.create_polygon([RA[0]-10,RA[1]+2,RA[0]+10,RA[1]+2,RA[0]+15,RA[1]+12,RA[0]-15,RA[1]+12],fill="white")
    # Thigh Joint
    C.create_oval(RH[0]-14,RH[1]-14,RH[0]+14,RH[1]+14,fill = "white")
    C.create_oval(RH[0]-12,RH[1]-12,RH[0]+12,RH[1]+12,fill = "black")
    # Knee Joint
    C.create_oval(RK[0]-10,RK[1]-10,RK[0]+10,RK[1]+10,fill = "white")
    C.create_oval(RK[0]-8,RK[1]-8,RK[0]+8,RK[1]+8,fill = "black")
    # Ankle Joint
    C.create_oval(RA[0]-8,RA[1]-8,RA[0]+8,RA[1]+8,fill = "white")
    C.create_oval(RA[0]-6,RA[1]-6,RA[0]+6,RA[1]+6,fill = "black")

    # Body 
    C.create_polygon([LS[0],LS[1]-15,((LS[0]+RS[0])//2 +1),LS[1]-3,RS[0]+2,RS[1]-15,RH[0]+13,RH[1]-10,(LH[0]+RH[0])//2,RH[1]+10,LH[0]-13,LH[1]-10],fill="gray")
    C.create_polygon([LS[0]+3,LS[1]-12,((LS[0]+RS[0])//2 +1),LS[1],RS[0]-1,RS[1]-12,RH[0]+10,RH[1]-13,(LH[0]+RH[0])//2,RH[1]+7,LH[0]-10,LH[1]-13],fill="white")

    # Boxes
    



def Make_Canvas(C,coordinates,root) :
    draw_stickman(C,coordinates,"black","enable_swords")
    root.update()
    time.sleep(0.2)
    C.delete('all')
    