#This program contains an outdoor scene of a house
#should have
    ## Three rectangles
    ## 2 lines
    ## 1 circle
    ## 1 text label

from graphics import *

def main():
    #create graphics window 
    win = GraphWin("My Home", 800, 650)
    win.setBackground("light blue")

    #draw line for grass
    line = Line(Point(1, 484), Point(799, 484))
    line.setWidth(350)
    line.setFill("green")
    line.draw(win)
    
    #draw rectangle for home
    home = Rectangle(Point(120, 205), Point(724, 505))
    home.setFill("light pink")
    home.draw(win)
    
    #draw door for home
    door = Rectangle(Point(344, 368), Point(445, 501))
    door.setFill("red")
    door.setOutline("black")
    door.draw(win)
    
    #create a door knob for door
    knob = Circle(Point(430, 443), 5)
    knob.setFill("black")
    knob.draw(win)
    
    #create lower right window
    lowRightWin = Rectangle(Point(541, 394), Point(641, 463))
    lowRightWin.setFill("light gray")
    lowRightWin.setOutline("black")
    lowRightWin.draw(win)
    #low right window line design
    line1 = Line(Point(591, 394), Point(591, 464))
    line1.draw(win)
    line2 = Line(Point(542, 428), Point(642, 428))
    line2.draw(win)
    
    #create upper right window
    upRightWin = lowRightWin.clone()
    upRightWin.move(3, -120)
    upRightWin.draw(win)
    line3 = Line(Point(594, 274), Point(594, 344))
    line3.draw(win)
    line4 = Line(Point(545, 310), Point(645, 310))
    line4.draw(win)
    
    #create left upper window
    leftUpWin = upRightWin.clone()
    leftUpWin.move(-350, 3)
    leftUpWin.draw(win)
    line5 = Line(Point(243, 277), Point(243, 346))
    line5.draw(win)
    line6 = Line(Point(194, 312), Point(294, 312))
    line6.draw(win)
    
    #create circle for sun
    sun = Circle(Point(655, 68), 60)
    sun.setFill("yellow")
    sun.draw(win)
    
    #create button text label for Animation
    button = Text(Point(395, 554), "CLICK ME!")
    button.setOutline("black")
    button.setStyle("bold")
    button.setSize(30)
    button.draw(win)
    Rectangle(Point(222, 520), Point(542, 600)).draw(win)
    
    #wait for user mouse click
    win.getMouse()
    
    #Night time animation
    win.setBackground("black")
    sun.setFill("whitesmoke")
    home.setFill("magenta")
    door.setFill("dark red")
    lowRightWin.setFill("gold")
    upRightWin.setFill("gold")
    leftUpWin.setFill("gold")
    line.setFill("dark green")
    star = Circle(Point(96, 40), 3)
    star.setFill("white")
    star.draw(win)
    button.setText("Good Night!")
    button.setSize(35)
    
    star2 = star.clone()
    star2.move(289, 131)
    star2.draw(win)
    star3 = star.clone()
    star3.move(356, 35)
    star3.draw(win)
    star4 = star.clone()
    star4.move(172, 110)
    star4.draw(win)
    star5 = star.clone()
    star5.move(676, 171)
    star5.draw(win)
    star6 = star.clone()
    star6.move(-24, 180)
    star6.draw(win)
    star7 = star.clone()
    star7.move(520, 120)
    star7.draw(win)
    
    #press good night to quit
    win.getMouse()
    win.close()
    
main()
