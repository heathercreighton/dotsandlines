# after variables lesson

# Constants
size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
distance_between_dots = size_of_board / number_of_dots 
dot_width = .25 * distance_between_dots
edge_width = .1 * distance_between_dots

# Functions
import numpy as np
def convert_to_logical_pos(xycoords): 
  grid_position = np.array(xycoords)
  position = (grid_position - distance_between_dots/4)//(distance_between_dots/2)

  type = False # Is it a row or a column?  Or False for neither.
  logical_position = []
  # Determine if the line clicked is a row or column
  if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
    r = int((position[0] -1)//2) # Which row
    c = int(position[1]//2) # Which column
    logical_position = [r, c]
    type = 'row'
  elif position[0] % 2 == 0 and (position[1] -1) % 2 == 0: 
    c = int((position[1] -1) // 2) # Column number
    r = int(position[0] // 2) # Row number
    logical_position = [r, c]
    type = 'col'

  return logical_position, type  

def playerClick(event):
  xycoords = [event.x, event.y]
  logical_position, valid_input = convert_to_logical_pos(xycoords)
  print(logical_position, valid_input)

def drawBoard(c):
  for i in range(number_of_dots): 
    x = i * distance_between_dots+distance_between_dots/2
    
    c.create_line(x, distance_between_dots/2, x, size_of_board - distance_between_dots/2, fill='gray', dash = (2,2))

    c.create_line(distance_between_dots/2, x, size_of_board - distance_between_dots/2, x, fill='gray', dash=(2,2))
  
def drawDots(c):
  for i in range(number_of_dots):
    for j in range(number_of_dots): 
      start_x = i * distance_between_dots + distance_between_dots/2
      end_x = j * distance_between_dots + distance_between_dots/2

      c.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill=dot_color, outline=dot_color)


# Create the board
from tkinter import *
window = Tk()
window.title("Dots and Line Game")
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack()
# Listen for user clicks
window.bind('<Button-1>', playerClick)
window.mainloop(30)
drawBoard(canvas)
drawDots(canvas)



# after tk intro