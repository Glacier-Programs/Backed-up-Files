import tkinter as tk
import loader
import tiles

#window
window = tk.Tk()
window.geometry('800x800')
window.title('Image Editor That Works Sort Of')

#variables
shapes_list = []
toolBarList = []

#for drawing
cur_shape = 0
colour='black'
size = 1
dragBtnVal = True
drag = True

#shapes
def circle(canvas,x,y,r,c='white',out=''):
    x0 = x-r
    y0 = y-r
    x1 = x+r
    y1 = y+r
    return canvas.create_oval(x0,y0,x1,y1,fill=c,outline=out)

def triangle(canvas,x,y,l,c='white'):
    x0 = x
    y0 = y-l
    x1 = x+l
    y1 = y+l
    x2 = x-l
    y2 = y+l
    coords=(x0,y0,x1,y1,x2,y2)
    return canvas.create_polygon(coords,fill=c)

def rect(canvas,x,y,h,w,c='white'):
    x0 = x-w//2
    y0 = y-h//2
    x1 = x0 + w
    y1 = y0
    x2 = x1
    y2 = y0 + h
    x3 = x0
    y3 = y2
    coords = (x0,y0,x1,y1,x2,y2,x3,y3)
    return canvas.create_polygon(coords,fill=c)

#functions
def clear(event=None):
    drawPad.delete('all')
    
def save():
    global save_entry, shapes_list
    file = save_entry.get()
    file = save_check(file)
    loader.save(shapes_list,file)

def save_check(file):
    meep = file.split('.')
    if meep[len(meep)-1] != '.pyimg':
        return file + '.pyimg'
    else:
        return file

def shape_change():
    global cur_shape
    cur_shape += 1
    return cur_shape

def draw(event):
    global cur_shape,colour,size
    x,y = event.x,event.y
    if cur_shape == 0:
        circle(drawPad,x,y,10*size,colour)
    elif cur_shape == 1:
        triangle(drawPad,x,y,10*size,colour)
    elif cur_shape == 2:
        rect(drawPad,x,y,20*size,20*size,colour)

def bigger():
    global size
    size +=1

def smaller():
    global size
    if size != 0:
        size -= 1

def Drag():
    #for setting drag value to true
    global dragBtnVal, drag
    if dragBtnVal:
        dragBtnVal = False
        drag = False
    else:
        dragBtnVal = True
        drag = True

def drag(event):
    #for letting the mouse drag
    global drag
    if drag:
            draw(event)

def set_mode_click():
    global toolBarList
    if toolBarList != []:
        hide()
    shape_btn.pack(side=tk.LEFT)
    colour_btn.pack(side=tk.LEFT)
    bigger_btn.pack(side=tk.LEFT)
    smaller_btn.pack(side=tk.LEFT)
    drag_btn.pack(side=tk.LEFT)
    clear_btn.pack(side=tk.LEFT)
    
    toolBarList.append(shape_btn)
    toolBarList.append(colour_btn)
    toolBarList.append(bigger_btn)
    toolBarList.append(smaller_btn)
    toolBarList.append(drag_btn)
    toolBarList.append(clear_btn)

def unset():
    #global
    pass

def set_mode_shape():
    pass

def set_mode_file():
    pass

def set_mode_insert():
    pass

def set_mode_paint():
    pass

def set_mode_tiles():
    hide()
    tiles.tileify()

def hide():
    global toolBarList
    for i in range(0,len(toolBarList)):
        toolBarList[i].pack_forget()

def colour_show():
    red_btn.pack(side=tk.LEFT)
    orange_btn.pack(side=tk.LEFT)
    yellow_btn.pack(side=tk.LEFT)
    green_btn.pack(side=tk.LEFT)
    blue_btn.pack(side=tk.LEFT)
    purple_btn.pack(side=tk.LEFT)
    white_btn.pack(side=tk.LEFT)
    grey_btn.pack(side=tk.LEFT)
    black_btn.pack(side=tk.LEFT)
    brown_btn.pack(side=tk.LEFT)
    custom_colour_entry.pack(side=tk.LEFT)
    custom_colour_btn.pack(side=tk.LEFT)

#toolbar
modeBar = tk.Frame(window)

file_mode_btn = tk.Button(modeBar,text='File',command=set_mode_file)
file_mode_btn.pack(side=tk.LEFT)
insert_mode_btn = tk.Button(modeBar,text='Insert',command=set_mode_insert)
insert_mode_btn.pack(side=tk.LEFT)
click_mode_btn = tk.Button(modeBar,text='Click',command=set_mode_click)
click_mode_btn.pack(side=tk.LEFT)
shape_mode_btn = tk.Button(modeBar,text='Shapes',command=set_mode_shape)
shape_mode_btn.pack(side=tk.LEFT)
tile_mode_btn = tk.Button(modeBar,text='Tiles',command=set_mode_tiles)
tile_mode_btn.pack(side=tk.LEFT)

modeBar.pack(fill=tk.X,side=tk.TOP)

toolBar = tk.Frame(window)

#multiple use buttons (not for file or insert modes)
clear_btn = tk.Button(toolBar,text='Clear',command=clear)
colour_btn = tk.Button(toolBar,text='Change Colour',command=colour_show)

#save mode buttons
file_lbl = tk.Label(toolBar,text='File:')
file_entry = tk.Entry(toolBar)
open_lbl = tk.Label(toolBar,text='Open:')
open_entry = tk.Label(toolBar)
save_btn = tk.Button(toolBar,text='Save')
save_as_btn = tk.Button(toolBar,text='Save As')
open_btn = tk.Button(toolBar,text='open')

#click mode buttons
shape_btn = tk.Button(toolBar,text='Change Shape',command=shape_change)
bigger_btn = tk.Button(toolBar,text='Bigger',command=bigger)
smaller_btn = tk.Button(toolBar,text='Smaller',command=smaller)
drag_btn = tk.Radiobutton(toolBar,text='Draggable?',command=Drag)

#shape mode buttons
circle_btn = tk.Button(toolBar,text='Circle')
rectangle_btn = tk.Button(toolBar,text='Rectangle')
free_form_btn = tk.Button(toolBar,text='Free Form')

#paint mode buttons


#makes tool bar appear
set_mode_click()
toolBar.pack(fill=tk.X)

subBar = tk.Frame(window)

#colours
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
def white():
    global colour
    colour = 'white'
def grey():
    global colour
    colour = 'grey'
def black():
    global colour
    colour = 'black'
def brown():
    global colour
    colour = 'brown'
def custom_colour():
    global colour
    colour = custom_colour_entry.get()

red_btn = tk.Button(subBar,bg='red',command=red)
orange_btn = tk.Button(subBar,bg='orange',command=orange)
yellow_btn = tk.Button(subBar,bg='yellow',command=yellow)
green_btn = tk.Button(subBar,bg='green',command=green)
blue_btn = tk.Button(subBar,bg='blue',command=blue)
purple_btn = tk.Button(subBar,bg='purple',command=purple)
white_btn = tk.Button(subBar,bg='white',command=white)
grey_btn = tk.Button(subBar,bg='grey',command=grey)
black_btn = tk.Button(subBar,bg='black',command=black)
brown_btn = tk.Button(subBar,bg='brown',command=brown)
custom_colour_entry = tk.Entry(subBar)
custom_colour_btn = tk.Button(subBar,command=custom_colour)

subBar.pack(fill=tk.X)

#the canvas
drawPad = tk.Canvas(window,bg='white',height=780,width=800)
drawPad.pack(fill=tk.X)

drawPad.bind('<Button-1>',draw)
drawPad.bind('<B1-Motion>',drag)

window.bind('c',clear)

window.mainloop()