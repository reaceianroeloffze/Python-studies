# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    # call the draw_ grid function
    draw_grid(canvas, scene_width, scene_height, 50)
    
    # call the draw_sky function
    draw_sky(canvas, scene_width, scene_height)
    
    # call the draw_ground fuction
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

# define a function to draw a grid
def draw_grid(canvas, width, height, interval): # Fuction to draw a grid
    # draw vertical lines
    y_label = 10
    for x in range(interval, width, interval):
        draw_line(canvas, x, 20, x, height, fill='navyBlue')
        draw_text(canvas, x, y_label, f'{x}', fill='navyBlue')
    # draw horizontal lines
    x_label = 10
    for y in range(interval, width, interval):
        draw_line(canvas, 23, y, width, y, fill='navyBlue')
        draw_text(canvas, x_label, y, f'{y}', fill='navyBlue')

# define the draw_sky function
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 150, scene_width, scene_height, outline='skyBlue', fill='midnightBlue')
    
    # randomly draw stars in the sky
    min_diameter = 3
    max_diameter = 3
    for stars in range(200):
        x = random.randint(0, scene_width)
        y = random.randint(150, scene_height)
        d = random.randint(min_diameter, max_diameter)
        draw_oval(canvas, x, y, x + d, y + d, fill='white')
        
    # Call the draw_clouds function
    draw_clouds(canvas)
    
    # Call the draw_building function
    draw_building(canvas)
    
# define function to draw clouds
def draw_clouds(canvas):
    draw_oval(canvas, 200, 475, 500, 350, outline='gray10', fill='gray10')
    draw_oval(canvas, 400, 450, 750, 300, outline='gray10', fill='gray10')
    draw_oval(canvas, 150, 400, 700, 200, outline='gray10', fill='gray10')
    
# Define a function to draw a building
def draw_building(canvas):
    draw_polygon(canvas, 700, 150, 100, 150, 100, 300, 50, 300, 100, 350, 700, 350, 750, 300, 700, 300, fill='black')
    
    # draw windows on the distant building
    side_1 = 5
    side_2 = 5
    side = side_1 * side_2
    space = 5
    interval = space * side / 2
    y = 185
    for floor in range(2):
        x = 105
        for cell in range(10):
            draw_rectangle(canvas, x, y, x + side, y + side, outline='khaki1', fill='khaki1')
            x += interval
        y += interval

# define the draw_ground function
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle (canvas, 0, 0, scene_width, 150, outline='springGreen3', fill='springGreen3')

    # call the draw_road function
    draw_road(canvas, scene_width)
    
    # call and loop the draw_lane_line function
    for x in range(100, 750, 100):
        draw_lane_line(canvas, x, 75, 50)
    
# Define a function to draw a road
def draw_road(canvas, scene_width):
    draw_rectangle(canvas, 0, 10, scene_width, 140, outline='gray10', fill='gray10')

# define function to draw a lane line on the road
def draw_lane_line(canvas, x_centre, y_centre, height):
    line_height = height / 10
    line_start = x_centre / 2
    line_end = x_centre + 50
    line_top = y_centre + line_height
    line_bottom = y_centre - line_height
    draw_rectangle (canvas, line_start, line_bottom, line_end, line_top, outline='white', fill='white')
    
# Call the main function so that
# this program will start executing.
main()