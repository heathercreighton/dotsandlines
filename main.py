from tkinter import *

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
dot_width = 0.25 *  distance_between_dots
edge_width = 0.10 * distance_between_dots

window = Tk()
window.title("Dots and Line Game")
window.mainloop(30)
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack() 


def draw_board(canvas):
  for l in range(50, 650,100):
    canvas.create_line(50,l,550, l, fill="blue", dash=(2,2))
    canvas.create_line(l, 50, l, 550, fill='blue', dash=(2,2)) 



  for i in range(6):
      for j in range(6):
          start_x = i * 100 + 50
          end_x = j * 100 + 50
          canvas.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill=dot_color, outline=dot_color)



def handle_click(event):
    print("someone clicked", event.x, event.y)


draw_board(canvas)
window.bind('<Button-1>', handle_click)



