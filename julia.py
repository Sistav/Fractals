# Program     : Julia Sets
# Name        : Georgios Dialynas-Vatsis
# Date        : Dec 12, 2023
# Description : Generates julia set fractals with colors depicting the stability of the numbers
import tkinter
from Complex import Complex

# This changes the maximum for the x and y axis, the smaller the number, the more zoomed in the image becomes
SCALE_WIDTH = 2
SCALE_HEIGHT = 2

# Window Width and height
WIDTH = 800    
HEIGHT = 800

# How many checks before determinining if a value is stable or unstable
# if you surpass ~250 it won't have proper color.
ITERATIONS = 100

# change these to change the choice of julia set   
c_x = -.70
c_y = .40

def tkinter_to_cartesian(x,y):
    # Convert tkinter coordinates to the cartesian plane

    # Get midpoints
    zero_x = (WIDTH/2)
    zero_y = (HEIGHT/2)
    
    # Use midpoints to find relative point, then multiply it by the scale
    final_x = ((x - zero_x) / (zero_x)) * SCALE_WIDTH
    final_y = ((y - zero_y) / (zero_y)) * SCALE_HEIGHT * -1 # -1 because the y axis is flipped to tkinter

    return final_x,final_y

# Create the window
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width = WIDTH, height = HEIGHT, bg = "black")

# Create the image and sticks it on the canvas
img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img)
window.title(f"{ITERATIONS} Iterations, Georgios D-V")

# For each pixel in the window
for tkinter_x in range(WIDTH):
    for tkinter_y in range(HEIGHT):

        # Convert each pixel to a number on the cartesian plane
        it_x,it_y = tkinter_to_cartesian(tkinter_x,tkinter_y)

        z = Complex(it_x,it_y)
        c = Complex(c_x,c_y)
 
        # Using this boolean instead of a break
        broken = False

        # i is our iterator
        i = 0
        while (i < ITERATIONS):
            i += 1

            # Square the current number and add c to it
            z = (z * z) + c

            # If it exceeds 2 then it is unstable, because no unstable number will ever pass 2
            if (z.imaginary > 2 or z.real > 2):

                # Calculate how dark a red to make the pixel by using how quickly the number because unstable
                red_amount = hex(int(i * 255 / ITERATIONS))
                if (len(red_amount) < 4):
                   red_amount += '0' 
                color = f"#{red_amount[2:]}0000"

                # Place the pixel on the image
                img.put(color, (tkinter_x, tkinter_y))
                break


        else:
            # If the number is to our knowledge stable, then color it white
            img.put("white",(tkinter_x,tkinter_y))  
        

    # Print perentage
    percent = int((tkinter_x/WIDTH)*1000) / 10
    print(f"{percent}%")


# x and y axis lines
canvas.create_line(WIDTH/2, 0,  WIDTH/2 , HEIGHT, fill = "white")
canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, fill = "white")

# Run it
canvas.pack()   
tkinter.mainloop()