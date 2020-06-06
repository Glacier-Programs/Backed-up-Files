import tkinter as tk
import random as r

matrix = []
opened_boxes = []
flags = 15
numx = 8
numy = 8
hp = 3

window = tk.Tk()
window.geometry('800x820')
window.title('MineSweeper')

#this stuff is for setting up a board
def place_bombs(bomb_num):
    global numx, numy
    print(bomb_num)
    taken = []
    for i in range(0,bomb_num):
        checking = True
        while checking:
            redo = False
            testx = r.randint(0,numx)
            testy = r.randint(0,numy)
            if testx == numx:
                testx -= 1
            if testy == numy:
                testy -= 1
            if i == 0:
                checking = False            
            for j in range(0,len(taken)):
                if taken[j] == [testx,testy]:
                    redo = True
            if not redo:
                checking = False
        taken.append([testx,testy])
    return taken

def matrix_up():
    global matrix,numx,numy
    matrix = []
    bombs = place_bombs(15)
    print(bombs)
    #bombs first bc algorithem checks matrix to see if there's bombs in any given spot
    for i in range(0,numy):
        line = []
        for j in range(0,numx):
            #check if current spot is a bomb
            for l in range(0,len(bombs)):
                cur = bombs[l]
                if i == cur[0] and j == cur[1]:
                    line.append('b')
            if len(line) != j-1:
                line.append('')
        matrix.append(line)
    print(matrix)
    for i in range(0,numy):
        line = matrix[i]
        for j in range(0,numx):
            num = 0
            if line[j] != 'b':
                #this is the better method
                up = False
                down = False
                left = False
                right = False
                if i != 0:
                    up = True
                if i != numy-1:
                    down = True
                if j != 0:
                    left = True
                if j != numx-1:
                    right = True
                if up:
                    if left:
                        if matrix[i-1][j-1] == 'b':
                            num += 1
                    if matrix[i-1][j] == 'b':
                        num += 1
                    if right:
                        if matrix[i-1][j+1] == 'b':
                            num += 1
                if left:
                    if matrix[i][j-1] == 'b':
                        num += 1
                if right:
                    if matrix[i][j+1] == 'b':
                        num += 1
                if down:
                    if left:
                        if matrix[i+1][j-1] == 'b':
                            num += 1
                    if matrix[i+1][j] == 'b':
                        num += 1
                    if right:
                        if matrix[i+1][j+1] == 'b':
                            num += 1
                matrix[i][j] = num

def set_up():
    global matrix, numx, numy, hp, opened_boxes
    hp = 3
    opened_boxes = []
    canvas.delete('all')
    for i in range(0,numx):
        spot = i * (800 / numx)
        canvas.create_line(spot,0,spot,800,fill='grey')
    for i in range(0,numy):
        spot = i * (800 / numy)
        canvas.create_line(0,spot,800,spot,fill='grey')
    matrix_up()
    health.configure(text='Health: '+str(hp))

#this stuff is for when the board is clicked
def onclick(event):
    global numx, numy, matrix, opened_boxes, hp
    if numx == 0 and numy == 0:
        return
    x,y = event.x,event.y
    print(x,y)
    square = [int(x//(canvas.winfo_width()/numx)),int(y//(canvas.winfo_height()/numy))]
    print(square)
    #this just checks if the square was already clicked
    opened = False
    if len(opened_boxes) > 0:
        for i in range(0,len(opened_boxes)):
            if square == opened_boxes[i]:
                opened = True
    #this gets the value of the square from the matrix 
    if not opened:
        beta_val = matrix[square[0]]
        val = beta_val[square[1]]
        val = str(val).split('f')
        print(val)
        box_width = canvas.winfo_width()/numx
        box_height = canvas.winfo_height()/numy
        if val[0] != '':
            if val[0] != 'b':
                canvas.create_text(square[0]*box_width+(box_width/2),square[1]*box_height+(box_height/2),text=str(val[0]))
            elif val[0] == 'b':
                canvas.create_rectangle(square[0]*box_width,square[1]*box_height,square[0]*box_width+box_width,square[1]*box_height+box_height,fill='black')
                hp -= 1
                health.configure(text='Health: '+str(hp))
            opened_boxes.append(square)
            if hp == 0:
               set_up()

def flag(event):
    global numx,numy, matrix, opened_boxes, flags
    if numx == 0 and numy == 0:
        return
    x,y = event.x,event.y
    print(x,y)
    square = [int(x//(canvas.winfo_width()/numx)),int(y//(canvas.winfo_height()/numy))]
    print(square)
    #this just checks if the square was already clicked
    opened = False
    if len(opened_boxes) > 0:
        for i in range(0,len(opened_boxes)):
            if square == opened_boxes[i]:
                opened = True
    bval = matrix[square[0]]
    val = bval[square[1]]
    print(val)
    cval = str(val).split('f')
    print(cval)
    if not opened and cval[0] != '':
        box_width = canvas.winfo_width()/numx
        box_height = canvas.winfo_height()/numy
        canvas.create_rectangle(square[0]*box_width,square[1]*box_height-1,square[0]*box_width+box_width,square[1]*box_height+box_height-1,fill='red')
        cval = 'f'+str(val)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if i == square[1] and j == square[0]:
                    matrix[j][i] = cval
        flags -= 1
        flags_lbl.configure(text='Flags: '+str(flags))
    elif not opened:
        box_width = canvas.winfo_width()/numx
        box_height = canvas.winfo_height()/numy
        canvas.create_rectangle(square[0]*box_width,square[1]*box_height-1,square[0]*box_width+box_width,square[1]*box_height+box_height-1,fill='white',outline='grey')
        aval = val[1]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if i == square[1] and j == square[0]:
                    matrix[j][i] = aval
        flags += 1
        flags_lbl.configure(text='Flags: '+str(flags))

def submit():
    global numx, numy
    #updates user settings
    val = numx
    try:
        numx = int(x_entry.get())
    except TypeError:
        numx = val
    val = numy
    try:
        numy = int(y_entry.get())
    except TypeError:
        numx = val
    set_up()

canvas = tk.Canvas(window,height=800,width=800,bg='white')
canvas.pack()

frame = tk.Frame(window)
health = tk.Label(frame,text='Health: '+str(hp))
health.pack(side=tk.LEFT)
flags_lbl = tk.Label(frame,text='Flags: '+str(flags))
flags_lbl.pack(side=tk.LEFT)
reset_btn = tk.Button(frame,text='Reset',command=set_up)
reset_btn.pack(side=tk.LEFT)
x_lbl = tk.Label(frame,text='X:')
x_lbl.pack(side=tk.LEFT)
x_entry = tk.Entry(frame)
x_entry.pack(side=tk.LEFT)
y_lbl = tk.Label(frame,text='Y:')
y_lbl.pack(side=tk.LEFT)
y_entry = tk.Entry(frame)
y_entry.pack(side=tk.LEFT)
submit_btn = tk.Button(frame,text='Submit',command=submit)
submit_btn.pack(side=tk.LEFT)
frame.pack(side=tk.TOP)

canvas.bind('<Button-1>',onclick)
canvas.bind('<Button-3>',flag)

set_up()

window.mainloop()