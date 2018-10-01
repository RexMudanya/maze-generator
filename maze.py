import turtle #imports the graphics library turtle

screen=turtle.Screen() #Creates the screen
screen.title("Maze") #Set the screens title to maze

#class that will draw the four sided cells/squares
def draw_cells(t,x,y,s):
	t.penup() #lifts the drawing symbol
	t.goto(x,y) #moves pointer to "new center"
	t.pendown() #draws visibly
	#loop to draw the square
	for i in range(0,4):
		board.forward(s) 
		board.left(90)

board = turtle.Turtle() #places pointer on screen

start_x = -180 #Sets starting point for the x-axis
start_y = 0 #Sets starting point for the x-axis
cell_size = 60 #Sets pixel size for each cell

#Sets the N*M of the rectangular array of cells
n = 4
m = 4   

#loop that draws all the small squares
for i in range(0,n): #Height
	for j in range(0,m): #width
		draw_cells(board,start_x + j*cell_size, start_y + i*cell_size, cell_size)
		print(start_x+j*cell_size) #startting at x
		print(start_y+i*cell_size) # starting at y

#Creating paths in the maze
board.penup()
board.color("white")
board.goto(-180,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-180,120)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-120,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-120,120)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-120,180)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-60,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-60,180)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(0,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(0,120)
board.pendown()
board.forward(cell_size)

board.penup()
board.goto(-120,120)
board.pendown()
board.left(90)
board.forward(cell_size)
board.penup()
board.goto(-120,180)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-60,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(0,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(0,120)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(0,180)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(-180,60)
board.pendown()
board.forward(cell_size)
board.penup()
board.goto(60,0)
board.pendown()
board.forward(cell_size)





turtle.done() #positions the screen so that it doesnt disappear
