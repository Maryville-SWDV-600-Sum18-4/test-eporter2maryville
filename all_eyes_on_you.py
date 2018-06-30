# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: Final Exam Practical problem #2

#####The images from the question are not viewable. I would have to download them which would take me out of the test.
#####I am creating my solution based purely on the text description.

#PseudoCode

# Create a Class for drawing the eyeballs
## Will need the centerpoint and window passed
## will need a move function to move the pupil
#draw the window and fill it with a color that makes the eyes standout
#create the 5 eyes
# create a clickpoint
## get the x for the clickpoint
#move the pupils in accordance with the x of the clickpoint

from graphics import *

class Eye:
    def __init__(self, centerPoint, window):
        self.center = centerPoint
        self.window = window
        
        self.sclera = Circle(centerPoint, 30)
        self.sclera.setFill( 'white' )
        self.sclera.draw( window )
        
        self.pupil = Circle(centerPoint, 10)
        self.pupil.setFill( 'black')
        self.pupil.draw( window )
        
        self.pupilLeft = int(centerPoint.x)-20
        self.pupilRight = int(centerPoint.x) + 20
        
        self.leftCenter = Point(self.pupilLeft,self.center.y)
        self.rightCenter = Point(self.pupilRight,self.center.y)
        
    def undrawPupil(self):
        self.pupil.undraw()
        
    def movePupil(self, newCenterPoint, window):
        self.undrawPupil()
        
        if newCenterPoint.x < self.pupilRight and newCenterPoint.x > self.pupilLeft:
            self.pupil = Circle(Point(newCenterPoint.x,self.center.y),10)
            self.pupil.setFill ('black')
            self.pupil.draw(window)
        elif newCenterPoint.x <= self.pupilLeft:
            self.pupil = Circle(self.leftCenter, 10)
            self.pupil.setFill ('black')
            self.pupil.draw(window)
        elif newCenterPoint.x >= self.pupilRight:
            self.pupil = Circle(self.rightCenter,10)
            self.pupil.setFill ('black')
            self.pupil.draw(window)
        
        #self.pupil = Circle(newCenterPoint, 10)
        #self.pupil.setFill('black')
        #self.pupil.draw(window)
        
        
def main():
    win = GraphWin("5 Eyes on a Mouse", 440, 400)
    win.setBackground( 'dark blue' )
    eye1=Eye(Point(40,260), win)
    eye2=Eye(Point(130,40), win)
    eye3=Eye(Point(220,300), win)
    eye4=Eye(Point(310,190), win)
    eye5=Eye(Point(400,370), win)
    while True:
        mouseClick=win.getMouse()
        newCenterPoint=Point(mouseClick.x,200)
        eye1.movePupil(newCenterPoint, win)
        eye2.movePupil(newCenterPoint, win)
        eye3.movePupil(newCenterPoint, win)
        eye4.movePupil(newCenterPoint, win)
        eye5.movePupil(newCenterPoint, win)

main()