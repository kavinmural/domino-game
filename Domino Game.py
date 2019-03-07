#Author: Kavin Muralitharan & Pratik Mistry
#Date: March 31, 2016
#Purpose: To make a domino class program using OOP
#=============================================================

#IMPORTS
import random
from tkinter import*

#Classes

#Author: Kavin Muralitharan
#Date: March 31, 2016
#Purpose: To define a domino.
#Data Elements:
# value - the value of the domino (an integer from 0 to 6)
# size - the size of the domino in the range 50 - 80
# diameter - the diameter of the dots on the domino  
# gap - the gaps between the dots on the domino
# orientation - the orientation of the domino (vertical or horizontal)
# face-up status - returns if the domino is faced up 
#Methods:
# __str__ - returns the value as a string
# getValue - gets the value and ensures it is a valid number
# setValue - sets the value to a valid number
# setSize - sets the size of the domino
# Randomize - randomizes numbers in the range 0-6
# draw - draws the skeleton of the domino on the canvas
# drawDots - draws the dots on the domino

class Domino:
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: Sets values to various objects
    # Parameters: value,orientation,faceUp
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __init__(self,value=1,orientation="H",faceUp = True,size=50):
        if size >= 30 or size <= 80:
            self.size = size
        else:
            size = 50
        self.value =  value
        self.size = int(var.get())
        self.diameter = self.size/5
        self.gap = self.diameter/2
        self.orientation = "H"
        self.faceUp = faceUp


    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: Return Value of domino as string
    # Parameters: None
    # Return: None
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    def __str__(self):
        self.value = str(value)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To get the value of the domino
    # Parameters: None
    # Return: None
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    def getValue(self):
        value1 = getPositiveInteger()
        value2 = getPositiveInteger()
        self.value = int(str(value1)+str(value2))
        
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To set the value
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def setValue(self):
        if self.value/10 > 6 or self.value%10 > 6 or self.value/10 < 0 or self.value%10 < 0:
            value = self.value 
        else:
            value = 1
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To flip the domino
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def flip(self):
        flipped = str(self.value)[::-1]
        self.value = int(flipped)
            
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To set the orientation of the domino
    # Parameters: none  
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-               
    def setOrientation(self, orientation):
        if orientation == 'V' or orientation == 'H':
            self.orientation = orientation
        else:
            orientation = 'H'
            
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose:  To set the size of the domino
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def setSize(self):
        if size >= 50 or size <=80:
            self.size = int(var.get())

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To randomize the values
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def randomize(self):
        self.value = int(str(random.randrange(0,7)) + str(random.randrange(0,7)))
        
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To draw the rectangle of the domino
    # Parameters: canvas,x,y
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def draw(self,canvas, x = 10, y = 10):
        if self.orientation == "H":
            canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 2, fill = "red")
            canvas.create_rectangle(x + self.size, y, self.size * 2 + x ,y + self.size, width = 2, fill = "red")
            self.drawDots(self.value//10,x,y)
            self.drawDots(self.value % 10,x + self.size, y)
                        
        else:
            canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 2, fill = "red")
            canvas.create_rectangle(x, y + self.size, x + self.size ,y + 2 * self.size, width = 2, fill = "red")
            self.drawDots(self.value//10,x,y)
            self.drawDots(self.value % 10,x, y+self.size)


    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: To draw the dots according to the value
    # Parameters: value,x,y 
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def drawDots(self,value,x,y):
            if self.orientation == "V":
                if value == 1:
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")   
                elif value == 2:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 3:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 4:            
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 5:
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 6:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotTwo = canvas.create_oval(x + self.gap, y + self.gap * 2 + self.diameter, x + self.gap + self.diameter, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "white", outline = "white")
                    self.dotSix = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap * 2 + self.diameter, x + self.gap * 3 + self.diameter*3, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")

            else:
                if value == 1:
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")  
                elif value == 2:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 3:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 4:            
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 5:
                    self.dotThree = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "white", outline = "white")
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                elif value == 6:
                    self.dotOne = canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotTwo = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap, x + self.gap * 2 + self.diameter * 2, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFour = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "white", outline = "white")
                    self.dotFive = canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                    self.dotSix = canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.size - self.gap, x + self.gap * 2 + self.diameter * 2, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
                    self.dotSeven = canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "white", outline = "white")
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To add two objects
    # Parameters: given radical (x)
    # Return: their sum
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __add__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "Sum:"+str(x.value + self.value)
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To subtract two objects
    # Parameters: given radical (x)
    # Return: their difference
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __sub__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "Difference:"+ str(x.value - self.value)
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To multiply two objects
    # Parameters: given radical (x)
    # Return: their product
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __mul__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "Product:"+str(x.value * self.value)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To return if x > value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __gt__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return ">" + str(x.value > self.value)
        

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x < value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __lt__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "<" + str(x.value < self.value)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x >= value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __ge__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return ">=" + str(x.value >= self.value)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x <= value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __le__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "<=" + str(x.value <= self.value)
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x equal to value 
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __eq__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "=" + str(x.value == self.value)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x does not equal value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __ne__(self,x):
        if self.value//10 > self.value%10:
            self.flip()
        if x.value//10 > x.value%10:
            x.flip()
        return "!=" + str(x.value != self.value)
        
#Author: Kavin Muralitharan & Pratik Mistry
#Date: April 12, 2016
#Purpose: To define a hand.
#Data Elements:
# size - the size of the domino in the range 50 - 80
#Methods:
# __str__ - returns the value as a string
# setSize - sets the size of the domino
# sort - sorts the dominos in order from least to greatest
# roll - randomizes the dominios    
# draw - draws dominos on canvas
# getRun - determines whether the run is 1,2 or 3


class Hand:
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: Sets values to various objects
    # Parameters: domino1,domino2,domino3,size
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __init__(self,domino1,domino2,domino3,size=60):
        if size >= 30 or size <= 80:
            size = size
        else:
            size = 50
        self.domino1 = domino1
        self.domino2= domino2
        self.domino3 = domino3


    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: March 8, 2016
    # Purpose: Return Value of domino as string
    # Parameters: None
    # Return: handValue
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
    def __str__(self):
        handValue = str(self.domino1) + "-" + str(self.domino2) + str(self.domino3)
        return handValue
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 12, 2016
    # Purpose: Sorts dominos in ascending order
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def sort(self):
        big = self.domino1.value
        mid = self.domino2.value
        small = self.domino3.value

        if(small > big):
            big, small = small, big
        if(mid > big):
            big,mid = mid,big
        if(small > mid):
            mid, small = small, mid

        self.domino1.value = small
        self.domino2.value = mid
        self.domino3.value = big


    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 12, 2016
    # Purpose: randomizes the dominos in the hand
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def roll(self):
        self.domino1.randomize()
        self.domino2.randomize()
        self.domino3.randomize()
        
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 12, 2016
    # Purpose: to draw dominos on the canvas
    # Parameters: none
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def draw(self):
        self.domino1.draw(canvas,20,20)
        self.domino2.draw(canvas,205,20)
        self.domino3.draw(canvas,390,20)
        
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 12, 2016
    # Purpose: determines the largest run of the hand
    # Parameters: n/a
    # Return: none
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def getRun(self):
        oneL = self.domino1.value // 10
        oneR = self.domino1.value % 10
        twoL = self.domino2.value  // 10
        twoR = self.domino2.value  % 10
        threeL = self.domino3.value  // 10
        threeR = self.domino3.value  % 10
        if oneL != twoL and oneL != twoR and oneL != threeL and oneL != threeR and twoL != threeL and twoL != threeR and twoR != threeR and twoR != threeL and oneR != twoR and oneR != twoL and oneR != threeL and oneR != threeR:
            run = 0
        elif oneL == twoL:
            if oneR == threeL or oneR == threeR or twoR == threeL or twoR == threeR:
                run = 3
            else:
                run = 2
            
        elif oneL == twoR:
            if oneR == threeL or oneR == threeR or twoL == threeL or twoL == threeR:
                run = 3
            else:
                run = 2

        elif oneL == threeL:
            if oneR == twoL or oneR == twoR or twoR == threeR or twoL == threeR:
                run = 3
            else:
                run = 2
            
        elif oneL == threeR:
            if oneR == twoL or oneR == twoR or twoL == threeL or twoR == threeL:
                run = 3
            else:
                run = 2
        
        elif oneR == twoL:
            if oneL == threeL or oneL == threeR or twoR == threeL or twoR == threeR:
                run = 3
            else:
                run = 2

        elif oneR == twoR:
            if oneL == threeL or oneL == threeR or twoL == threeL or twoL == threeR:
                run = 3
            else:
                run = 2
                
        elif oneR == threeL:
            if oneL == twoL or oneL == twoR or twoL == threeR or twoR == threeL:
                run = 3
            else:
                run = 2

        elif oneR == threeR:
            if oneL == twoL or oneL == twoR or twoL == threeL or twoR == threeL:
                run = 3
            else:
                run = 2

        elif twoL == threeL:
            if oneL == twoR or oneR == twoR or oneL == threeR or oneR == threeR:
                run = 3
            else:
                run = 2

        elif twoL == threeR:
            if oneL == twoR or oneR == twoR or oneL == threeL or oneR == threeL:
                run = 3
            else:
                run = 2

        elif twoR == threeL:
            if oneR == twoL or oneL == twoL or oneL == threeR or oneR == threeR:
                run = 3
            else:
                run = 2

        elif twoR == threeR:
            if oneL == twoL or oneR == twoL or oneL == threeL or oneR == threeL:
                run = 3
            else:
                run = 2
                
        return run
        
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To return if x > value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __gt__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return  ">"+str(b > a)
        

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x < value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __lt__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return  "<"+str(b < a)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x >= value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __ge__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return ">="+ str(b >= a)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x <= value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __le__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return "<="+ str(b <= a)
    
    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x equal to value 
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __eq__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return "="+str(b == a)

    # Author: Kavin Muralitharan & Pratik Mistry
    # Date: April 25, 2016
    # Purpose: To determine if x does not equal value
    # Parameters: given radical (x)
    # Return: boolean
    #-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def __ne__(self,x):
        a = self.domino1.value + self.domino2.value + self.domino3.value
        b = x.domino1.value + x.domino2.value + x.domino3.value
        return "!="+str(b != a)

    
#SUBS

# Author: Kavin Muralitharan & Pratik Mistry
# Date: March 2, 2016
# Purpose: To get Positive integer
# Parameters: intLow, intHigh
# Return: positive number
#-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def getPositiveInteger (intLow = 1, intHigh = 6):
    intNumber = self.value
    while intNumber < intLow or intNumber > intHigh:
        intNumber = str(input("Input a Positive Integer: "))
        while not intNumber.isdigit ():
            print("Your Input Was Not a Positive Integer!")
            intNumber = str(input("Input a Positive Integer: "))
        intNumber = int(intNumber)
        if intNumber < intLow or intNumber > intHigh:
            print("Your Integer Was Invalid, It Was Not in the Range")
        if intNumber/10 > 6 or intNumber%10 > 6:
            print("Your Number is invalid! You cannot enter a value with a digit greater than 6.")
    return intNumber

# Author: Kavin Muralitharan & Pratik Mistry
# Date: April 25, 2016
# Purpose: To display the hand of a domino
# Parameters: none
# Return: none
#-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def display():
    canvas.delete("all")
    domino1 = Domino()
    domino1.randomize()
    domino1.draw(canvas,20,20)
    domino2 = Domino()
    domino2.randomize()
    domino2.draw(canvas,205,20)
    domino3 = Domino()
    domino3.randomize()
    domino3.draw(canvas,390,20)
    hand = Hand(domino1, domino2,domino3)
    run = "The Run is: " + str(hand.getRun())
    hand.sort()
    domino1.draw(canvas,20,120)
    domino2.draw(canvas,205,120)
    domino3.draw(canvas,390,120)
    runLabel = Label(root,text=run,font = ("calibri",26,"bold"),fg= "black",bg="gainsboro")
    runLabel.place(x=355,y=350)

# Author: Kavin Muralitharan & Pratik Mistry
# Date: March 8, 2016
# Purpose: To bind a key
# Parameters: event
# Return: N/A
#-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def keyPressed(event):
    if event.char == "h":
        canvas.delete("all")
        domino1 = Domino()
        domino1.randomize()
        domino1.draw(canvas,20,20)
        domino2 = Domino()
        domino2.randomize()
        domino2.draw(canvas,205,20)
        domino3 = Domino()
        domino3.randomize()
        domino3.draw(canvas,390,20)
        hand = Hand(domino1, domino2,domino3)
        run = "The Run is: " + str(hand.getRun())
        hand.sort()
        domino1.draw(canvas,20,120)
        domino2.draw(canvas,205,120)
        domino3.draw(canvas,390,120)
        runLabel = Label(root,text=run,font = ("calibri",26,"bold"),fg= "black",bg="gainsboro")
        runLabel.place(x=355,y=350)
    
    elif event.char == "x":
        root.destroy()
        
    elif event.char == "g":
        count = 0
        zero = 0
        two = 0
        three = 0
        while count != 10000:
            domino1 = Domino()
            domino2 = Domino()
            domino3 = Domino()
            domino1.randomize()
            domino2.randomize()
            domino3.randomize()               
            hand = Hand(domino1,domino2,domino3)
            run = hand.getRun()
            if run == 0:
                zero = zero + 1
            elif run == 2:
                two = two + 1
            elif run == 3:
                three = three + 1
            count = count + 1
        zero = "Run Zero: " + str(zero)
        two = "Run Two: " + str(two)
        three = "Run Three: " + str(three)
        canvas.delete("all")
        canvas.create_text(80,30,text=zero,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(250,30,text=two,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(420,30,text=three,fill="white",font = ("calibri",16,"bold"))

    elif event.char == "o":
        canvas.delete("all")
        domino1 = Domino()
        domino2 = Domino()
        domino1.randomize()
        domino2.randomize()
        domino1.draw(canvas,20,20)
        domino2.draw(canvas,205,20)
        canvas.create_text(100,260,text=domino2+domino1,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(270,260,text=domino2-domino1,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(440,260,text=domino2*domino1,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(100,230,text=str(domino2>domino1),fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(270,230,text=str(domino2<domino1),fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(440,230,text=str(domino2>=domino1),fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(100,290,text=str(domino2<=domino1),fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(270,290,text=str(domino2==domino1),fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(440,290,text=str(domino2!=domino1),fill="white",font = ("calibri",16,"bold"))
        runLabel = Label(root,text="",font = ("calibri",26,"bold"),bg="#3f48ac")
        runLabel.place(x=355,y=350)

    elif event.char == "c":
        canvas.delete("all")
        domino1 = Domino()
        domino1.randomize()
        domino1.draw(canvas,20,20)
        domino2 = Domino()
        domino2.randomize()
        domino2.draw(canvas,205,20)
        domino3 = Domino()
        domino3.randomize()
        domino3.draw(canvas,390,20)
        hand1 = Hand(domino1,domino2,domino3)
        domino1 = Domino()
        domino1.randomize()
        domino1.draw(canvas,20,120)
        domino2 = Domino()
        domino2.randomize()
        domino2.draw(canvas,205,120)
        domino3 = Domino()
        domino3.randomize()
        domino3.draw(canvas,390,120)
        hand2 = Hand(domino1,domino2,domino3)
        canvas.create_text(100,250,text=hand1<hand2,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(270,250,text=hand1<hand2,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(440,250,text=hand1>=hand2,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(100,280,text=hand1<=hand2,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(270,280,text=hand1==hand2,fill="white",font = ("calibri",16,"bold"))
        canvas.create_text(440,280,text=hand1!=hand2,fill="white",font = ("calibri",16,"bold"))
        runLabel = Label(root,text="",font = ("calibri",26,"bold"),bg="#3f48ac")
        runLabel.place(x=355,y=350)

        
        
        
#MAIN
root = Tk()
root.title("Domino")
root.resizable(width=False,height=False)
canvas = Canvas(root,width=565,height=500)
canvas.config(background = "#3f48ac")

var = IntVar()
scale = Scale(root,from_=40,to=80,font=("Calibri",15,"bold"),orient = HORIZONTAL, variable = var, length = 280,bg = "gainsboro")
scale.pack(anchor=CENTER)
scale.place(x=20,y=350)
sizeLabel = Label(root, text="Size",font=("Calibri",15,"bold"),bg = "gainsboro")
sizeLabel.place(x=20,y=320)
       
canvas.bind("<Key>",keyPressed)
canvas.pack()
canvas.focus_set()

rollButton = Button (root, bg="gainsboro", text = "Roll",font=("Times New Roman",14,"bold"), width = 13,height = 1,command = lambda:display()).place (x=209,y=440)
exitButton = Button (root, bg="gainsboro", text = "Exit",font=("Times New Roman",14,"bold"), width = 13,height = 1,command = lambda:root.destroy()).place (x=396,y=440)
clearButton = Button (root, bg="gainsboro", text = "Clear",font=("Times New Roman",14,"bold"), width = 13,height = 1,command = lambda:canvas.delete("all")).place (x=20,y=440)


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit",command=lambda:root.destroy())
filemenu.add_command(label="New hand",command=lambda:display())
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

mainloop()


#Classes

#Author: Kavin Muralitharan & Pratik Mistry
#Date: June 6, 2016
#Purpose: To create a domino game
#Data Elements:
# table - the playing field of the dominos
# hands - four hands which will be used to play the game
# names - the names of each player (four in total)
# available - 
#Methods:
# setup - sets up the game, when the game starts
# getNames - gets the names of the players, from user input
# initAvailable - set only values with the first digit >= the second digit to true
# deal - deals out 7 cards to each of the players
# putHand - puts the ith hand
# canMove - returns true of the ith player can move
# firstMove - returns the player with 6|6 (the player with it goes first)
# getUsersMove - gets the value of the Domino and which end of the line to put it in
# getComputerMove - gets the ith hand computer player’s domino value to be played and side of the table to attach it to
# play - draws the game table, gets the names, deals, then goes through each player for their turns
 
class DominoGame:

    def __init__(self,table):
        hand1 = self.hand1
        hand2 = self.hand2
        hand3 = self.hand3
        hand4 = self.hand4
        table = self.table

    def setup(self):

    def getNames(self):
        
        
    


