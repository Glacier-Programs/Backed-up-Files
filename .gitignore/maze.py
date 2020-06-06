import tkinter as tk

xnum = 0
ynum = 0

s_matrix = []

def draw():
    global xnum, ynum, s_matrix
    s_width = canvas.winfo_width() / xnum
    s_height = canvas.winfo_height() / ynum
    print(s_width,s_height)
    for i in range(0,xnum):
        spot = i * s_width + s_width
        canvas.create_line(spot,0,spot,canvas.winfo_height())
    for i in range(0,ynum):
        spot = i * s_height + s_height
        canvas.create_line(0,spot,canvas.winfo_width(),spot)
    matrix_set()

def matrix_set():
    global s_matrix, xnum, ynum
    s_matrix = []
    for i in range(0,xnum):
        s_matrix.append([])
        for j in range(0,ynum):
            s_matrix[i].append(0)

def submit():
    global xnum, ynum
    canvas.delete('all')
    xnum = int(xentry.get())
    ynum = int(yentry.get())
    print(xnum,ynum)
    draw()

window = tk.Tk()
window.geometry('950x800')
window.title('Maze Maker')

debug = tk.Tk()
debug.geometry('300x300')
debug.title('Debug')

canvas = tk.Canvas(window,height=800,width=800,bg='white')
canvas.pack(side=tk.LEFT)

debug_canvas = tk.Canvas(debug,height=300,width=300,bg='white')
debug_canvas.pack(fill=tk.BOTH)

aframe = tk.Frame(window)

bframe = tk.Frame(aframe)
xlbl = tk.Label(bframe,text='Num on x axis:')
xentry = tk.Entry(bframe)
xlbl.pack(side=tk.LEFT)
xentry.pack(side=tk.LEFT)
bframe.pack()

cframe = tk.Frame(aframe)
ylbl = tk.Label(cframe, text="Num on y axis:")
yentry = tk.Entry(cframe)
ylbl.pack(side=tk.LEFT)
yentry.pack(side=tk.LEFT)
cframe.pack()

submit_btn = tk.Button(aframe,text='Submit',command=submit)
submit_btn.pack()

aframe.pack(side=tk.RIGHT)

#update debug screen
debug_lines = 0
def update_debug(string):
    global debug_lines
    debug_lines += 1
    debug_canvas.create_text(150,debug_lines*13,text=string)
    debug_canvas.update()

def find_square(x,y):
    global ynum, xnum
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    s_width = width / xnum
    s_height = height / ynum
    spotx = int(x // s_width)
    spoty = int(y // s_height)
    return [spotx,spoty]

def draw_square(square,mode):
    global xnum, ynum
    s_width = canvas.winfo_width() / xnum
    s_height = canvas.winfo_height() / ynum
    update_debug('Square width: '+str(s_width))
    update_debug('Square height: '+str(s_height))
    update_debug('Xnum: '+str(xnum))
    update_debug('Ynum: '+str(ynum))
    update_debug('Tlc: ('+str(square[0]*s_width)+','+str(square[1]*s_height)+')')
    update_debug('Brc: ('+str(square[0]*s_width+s_width)+','+str(square[1]*s_height+s_height)+')')
    if mode == 0:
        canvas.create_rectangle(square[0]*s_width, square[1]*s_height, square[0]*s_width+s_width, square[1]*s_height+s_height,fill='grey')
    if mode == 1:
        canvas.create_rectangle(square[0]*s_width, square[1]*s_height, square[0]*s_width+s_width, square[1]*s_height+s_height,fill='white')
    canvas.update()

def onclick(event):
    global s_matrix, debug_lines
    debug_canvas.delete('all')
    debug_lines = 0
    x,y = event.x,event.y
    update_debug('Mouse Coords: '+str(x)+','+str(y))
    square = find_square(x,y)
    update_debug('Square: '+str(square))
    s_val = s_matrix[square[0]][square[1]]
    draw_square(square,s_val)
    if s_val == 1:
        s_matrix[square[0]][square[1]] = 0
    else:
        s_matrix[square[0]][square[1]] += 1
    update_debug('Square value: ' + str(s_val+1))
    update_debug('Drawn')

canvas.bind('<Button-1>',onclick)

window.mainloop()