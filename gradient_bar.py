#create a gradient bar
#width of window must be 400

from graphics import *

def main():
    win = GraphWin("Gradient Bar", 400, 130)
    #Num of bars used must be a multiple of 6
    num = 6
    #need to divide the width by num to find the width of each rectangle
    rectWidth = 400 / num
    #equation to change the color value (intensity) 
    cValue = 255 // num
    #c for color
    c = 0
    #coordinate x is equal to 0
    x = 0
    #height of bars should be length of window. ht is for height
    ht = 130 
    
    #create a loop
    for i in range(num):
        rect = Rectangle(Point(x, 0), Point(x + rectWidth, ht))
        #convert int to hex value to get gradient. x means to print as hex and the 02 means pad 2 characters w/ 0.
        # % is used for formatting an rgb sequence -- 02x(r), 02x(g), 02x(b)
        gradient = color_rgb(255, 0, 0)
        rect.setFill(gradient)
        rect.setWidth(0)
        c = c + cValue
        x = x + rectWidth
        rect.draw(win)
       
    #click anywhere on screen with mouse to close program 
    win.getMouse()   
    win.close()

main()