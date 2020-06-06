import tkinter as tk
from time import sleep

window = tk.Tk()

width = 1000
height= 1250
acolour = 'white'

x = width // 4
y = 0
rad = 50

y_speed = 20
colour = 'red'

fps = 0.01

#physics stuff


#functions
def submit():
    global fps,y_speed,rad
    if fps_entry.get() != '':
        fps = int(fps_entry.get())/100
    if falling_speed.get() != '':
        y_speed = float(falling_speed.get())
    if rad_entry.get() != '':
        rad = float(rad_entry.get())
    
#colour functions
def red():
    global colour
    colour = 'red'

def orange():
    global colour
    colour = 'orange'

def yellow():
    global colour
    colour = 'yellow'

def green():
    global colour
    colour = 'green'

def blue():
    global colour
    colour = 'blue'

def purple():
    global colour
    colour = 'purple'

def black():
    global colour
    colour = 'black'

def white():
    global colour
    colour = 'white'

def grey():
    global colour
    colour = 'grey'

def brown():
    global colour
    colour = 'brown'

def ared():
    global acolour
    acolour = 'red'

def aorange():
    global acolour
    acolour = 'orange'

def ayellow():
    global acolour
    acolour = 'yellow'

def agreen():
    global acolour
    acolour = 'green'

def ablue():
    global acolour
    acolour = 'blue'

def apurple():
    global acolour
    acolour = 'purple'

def ablack():
    global acolour
    acolour = 'black'

def awhite():
    global acolour
    acolour = 'white'

def agrey():
    global acolour
    acolour = 'grey'

def abrown():
    global acolour
    acolour = 'brown'

canvas = tk.Canvas(window,bg='white',height=height,width=width//2)
canvas.pack(side=tk.LEFT)

frame = tk.Frame(window)

fs_lbl = tk.Label(frame,text='Falling Speed:')
fs_lbl.pack(side=tk.TOP,fill=tk.X)

falling_speed = tk.Entry(frame)
falling_speed.pack(side=tk.TOP,fill=tk.X)

fps_lbl = tk.Label(frame,text='Update Speed:')
fps_lbl.pack(side=tk.TOP,fill=tk.X)

fps_entry = tk.Entry(frame)
fps_entry.pack(side=tk.TOP,fill=tk.X)

rad_lbl = tk.Label(frame,text='Radius:')
rad_lbl.pack(side=tk.TOP,fill=tk.X)

rad_entry = tk.Entry(frame)
rad_entry.pack(side=tk.TOP,fill=tk.X)

submit_btn = tk.Button(frame,text='Submit',command=submit)
submit_btn.pack(side=tk.TOP,fill=tk.X)

colour_lbl = tk.Label(frame,text='Circle Colour:')
colour_lbl.pack(side=tk.TOP,fill=tk.X)

colour_frame = tk.Frame(frame)
#changes ball colour
red = tk.Button(colour_frame,bg='red',command=red)
red.grid(column=0,row=0)
orange = tk.Button(colour_frame,bg='orange',command=orange)
orange.grid(column=1,row=0)
yellow = tk.Button(colour_frame,bg='yellow',command=yellow)
yellow.grid(column=2,row=0)
green = tk.Button(colour_frame,bg='green',command=green)
green.grid(column=3,row=0)
blue = tk.Button(colour_frame,bg='blue',command=blue)
blue.grid(column=4,row=0)
purple = tk.Button(colour_frame,bg='purple',command=purple)
purple.grid(column=0,row=1)
white = tk.Button(colour_frame,bg='white',command=white)
white.grid(column=1,row=1)
grey = tk.Button(colour_frame,bg='grey',command=grey)
grey.grid(column=2,row=1)
black = tk.Button(colour_frame,bg='black',command=black)
black.grid(column=3,row=1)
brown = tk.Button(colour_frame,bg='brown',command=brown)
brown.grid(column=4,row=1)
colour_frame.pack(side=tk.TOP)

bg_lbl = tk.Label(frame,text='Background Colour:')
bg_lbl.pack(side=tk.TOP,fill=tk.X)

acolour_frame = tk.Frame(frame)
#changes background colour
ared = tk.Button(acolour_frame,bg='red',command=ared)
ared.grid(column=0,row=0)
aorange = tk.Button(acolour_frame,bg='orange',command=aorange)
aorange.grid(column=1,row=0)
ayellow = tk.Button(acolour_frame,bg='yellow',command=ayellow)
ayellow.grid(column=2,row=0)
agreen = tk.Button(acolour_frame,bg='green',command=agreen)
agreen.grid(column=3,row=0)
ablue = tk.Button(acolour_frame,bg='blue',command=ablue)
ablue.grid(column=4,row=0)
apurple = tk.Button(acolour_frame,bg='purple',command=apurple)
apurple.grid(column=0,row=1)
awhite = tk.Button(acolour_frame,bg='white',command=awhite)
awhite.grid(column=1,row=1)
agrey = tk.Button(acolour_frame,bg='grey',command=agrey)
agrey.grid(column=2,row=1)
ablack = tk.Button(acolour_frame,bg='black',command=ablack)
ablack.grid(column=3,row=1)
abrown = tk.Button(acolour_frame,bg='brown',command=abrown)
abrown.grid(column=4,row=1)
acolour_frame.pack(side=tk.TOP)

frame.pack(side=tk.LEFT,fill=tk.Y)

while True:
    if y >= height:
        y = 0
    canvas.delete('all')
    canvas.configure(bg=acolour)
    canvas.create_oval(x-rad,y-rad,x+rad,y+rad,fill=colour)
    y += y_speed
    canvas.update()
    window.update()
    sleep(fps)