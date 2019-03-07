#Author: Kavin Muralitharan & Pratik Mistry
#Date: June 1st, 2016
#Purpose: Culminating Task
#Input: GUI Interface
#Ouput: GUI Interface
#----------------------------------------------------------------------------------------
from tkinter import*
import random
from tkinter import messagebox

#Classes

#Author: Kavin Muralitharan
#Date: April 4, 2016
#Purpose: To Define A Domino
#Data Elements:
# value - Amount Of The Domino Dots
# size - Size Of The Domino
# diameter - The Diameter Of Each Dot (Controls Size Of Dot)
# gap - The Amount Of Gap Between The Side, and Another Dot
# orientation - The Orientation Of The Domino (Either H or V)
# faceup - Either Face Up or Not (Boolean)
# faceupvalue - Holds A Temp Value (Zero)
#Methods:
# getValue - Gets A Valid Value From The User And Returns It
# setValue - Checks A Number And Sets It As The Value (Data Element)
# flip - Flips The Digits Of The Value (Data Element)
# setOrientation - Validates The Parameter (orientation) And Sets It As The Orientation (Data Element)
# putFaceUp - Turns The Value To 0 And Holds A Back Up Value
# setSize - Checks The Given Parameter (size) And Sets It As The Size (Data Element)
# randomize - Sets The Value (Data Element) To A Random Integer Between 0 & 6
# draw - Draws Three Dominos
# drawDots - Makes The Dots Viewable Depending On The Value (Data Element)
# __str__ - Changes The Value (Data Element) Into A String, So It Can Be Printed
# __add__ - Adds The Values Of Two Dominos
# __add__(2) - Adds The Values Of A Domino And A Integer
# __sub__ - Subtracts The Values Of Two Dominos
# __mul__ - Multiplies The Values Of Two Dominos
# __gt__ - Checks If One Value Of A Domino Is Greater Than Another
# __lt__ - Checks If One Value Of A Domino Is Less Than Another
# __ge__ - Checks If One Value Of A Domino Is Greater Than Or Equal To Another
# __le__ - Checks If One Value Of A Domino Is Less Than Or Equal To Another
# __eq__ - Checks If One Value Of A Domino Is Equal To Another
# __ne__ - Checks If One Value Of A Domino Is Not Equal To Another
class Domino:
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Initialize The Object's Data Elements
    #Parameters: value, size, orientation and faceUp
    #Return: None
    def __init__(self, value = 1, size = 80, orientation = "H", faceUp = True):
        self.randomize()
        if value // 10 > 6 or value // 10 < 0 or value % 10 > 6 or value % 10 < 0:
            value = 0
        self.value = value
        self.size = size
        self.diameter = size / 5
        self.gap = self.diameter / 2
        self.orientation = orientation
        self.faceUp = faceUp
        self.faceUpValue = self.value
        
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Get A Valid Value From The User
    #Parameters: None
    #Return: The User's Input For Value
    def getValue(self):
        valueOne = input("Input A Value Between 0 to 6: ")
        while valueOne.isdigit == False or valueOne < 0 or valueOne > 6:
            print("Invalid Input!")
            valueOne = input("Input A Value Between 0 to 6: ")
        valueTwo = input("Input A Value Between 0 to 6: ")
        while valueTwo.isdigit == False or valueTwo < 0 or valueTwo > 6:
            print("Invalid Input!")
            valueTwo = input("Input A Value Between 0 to 6: ")
        value = int(valueOne + valueTwo)
        return value
    
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Set A Valid Value To The Value Data Element
    #Parameters: value
    #Return: None
    def setValue(self, value):
        if value // 10 <= 6 and value // 10 >= 0 and value % 10 <= 6 and value % 10 >= 0:
            self.value = value
            
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Reverse The Digits Of A Number And Set It As The Value Data Element
    #Parameters: value
    #Return: None    
    def flip(self, value):
        if value % 10 == value:
            flipped = value * 10
        else:
            flipped = str(value)[::-1]
            flipped = int(flipped)
        return flipped
            
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Set A Valid Value For The Orientation Data Element
    #Parameters: orientation
    #Return: None
    def setOrientation(self, orientation):
        if orientation == "V" or orientation == "H":
            self.orientation = orientation
        else:
            self.orientation = "V"

    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Determine Whether The Domino Is Face Up Or Not
    #Parameters: None
    #Return: None
    def putFaceUp(self):
        if self.faceUp == False:
            self.value = 0
        if self.faceUp == True:
            self.value = self.faceUpValue
    
    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Set A Valid Size To The Size Data Element
    #Parameters: size
    #Return: None
    def setSize(self, size):
        if size >= 30 and size <= 80:
            self.size = size
            self.diameter = self.size = 5
            self.gap = self.diameter / 2
        else:
            self.size = 30
            self.diameter = self.size / 5
            self.gap = self.diameter / 2

    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Randomly Generate A Two Digit Number (Both Digits Between 0 & 6) And Set It As The Value Data Element
    #Parameters: None
    #Return: None
    def randomize(self):
        valueOne = random.randrange(0,7)
        valueTwo = random.randrange(0,7)
        value = int(str(valueOne) + str(valueTwo))
        self.value = value

    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Draw The Dominos
    #Parameters: canvas, x, and y
    #Return: None
    def draw(self, canvas, x = 10, y = 10, place = 1):
        if self.orientation == "H":
            square1 = canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 2, fill = "#06000a", outline = "white")
            if self.faceUp == False:
                canvas.itemconfig(square1, outline = "blue")
            square2 = canvas.create_rectangle(x + self.size, y, self.size * 2 + x ,y + self.size, width = 2, fill = "#06000a", outline = "white")
            if self.faceUp == False:
                canvas.itemconfig(square2, outline = "blue")
            self.drawDots(canvas, x, y, self.value // 10)
            self.drawDots(canvas, x + self.size, y, self.value % 10)
        else:
            square3 = canvas.create_rectangle(x, y, x + self.size, y + self.size, width = 2, fill = "#06000a", outline = "white")
            if self.faceUp == False:
                canvas.itemconfig(square3, outline = "blue")
            square4 = canvas.create_rectangle(x, y + self.size, x + self.size ,y + 2 * self.size, width = 2, fill = "#06000a", outline = "white")
            if self.faceUp == False:
                canvas.itemconfig(square4, outline = "blue")
            self.drawDots(canvas, x, y, self.value // 10)
            self.drawDots(canvas, x, y + self.size, self.value % 10)

    #Author: Kavin Muralitharan
    #Date: April 4, 2016
    #Purpose: To Make The Appropriate Dots Visible Depending On The Value Data Element
    #Parameters: canvas, value, x, and y,
    #Return: None
    def drawDots(self, canvas, x, y, value):
        if self.orientation == "V":
            if value == 1:
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
            elif value == 2:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + (self.size - self.gap), x + (self.size - self.gap) - self.diameter, y + (self.size - self.gap) - self.diameter, fill = "White", outline = "White")
            elif value == 3:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + (self.size - self.gap), x + (self.size - self.gap) - self.diameter, y + (self.size - self.gap) - self.diameter, fill = "White", outline = "White")
            elif value == 4:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + self.gap, x + (self.size - self.gap) - self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + (self.size - self.gap), x + (self.size - self.gap) - self.diameter, y + (self.size - self.gap) - self.diameter, fill = "White", outline = "White")
            elif value == 5:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + self.gap, x + (self.size - self.gap) - self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + (self.size - self.gap), x + (self.size - self.gap) - self.diameter, y + (self.size - self.gap) - self.diameter, fill = "White", outline = "White")
            elif value == 6:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.gap * 2 + self.diameter, x + self.gap + self.diameter, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.gap * 3 + self.diameter * 2, x + self.gap + self.diameter, y + self.gap * 3 + self.diameter * 3, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + self.gap, x + (self.size - self.gap) - self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + self.gap * 2 + self.diameter, x + (self.size - self.gap) - self.diameter, y + self.gap * 2 + self.diameter + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + (self.size - self.gap), y + (self.size - self.gap), x + (self.size - self.gap) - self.diameter, y + (self.size - self.gap) - self.diameter, fill = "White", outline = "White")
        else:
            if value == 1:
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
            elif value == 2:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
            elif value == 3:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
            elif value == 4:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
            elif value == 5:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap * 2 + self.diameter, x + self.gap * 2 + self.diameter * 2, y + self.gap * 2 + self.diameter * 2, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
            elif value == 6:
                canvas.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.gap, x + self.gap * 2 + self.diameter * 2, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.gap, x + self.gap * 3 + self.diameter * 3, y + self.gap + self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap, y + self.size - self.gap, x + self.gap + self.diameter, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 2 + self.diameter, y + self.size - self.gap, x + self.gap * 2 + self.diameter * 2, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")
                canvas.create_oval(x + self.gap * 3 + self.diameter * 2, y + self.size - self.gap, x + self.gap * 3 + self.diameter * 3, y + self.size - self.gap - self.diameter, fill = "White", outline = "White")

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Make The Domino Printable
    #Parameters: None
    #Return: String
    def __str__(self):
        string = str(self.value // 10) + "/" + str(self.value % 10)
        return string
    
    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The + Operator To Add Objects (Values)
    #Parameters: dominoTwo
    #Return: totalSum
    def __add__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        totalSum = firstDomino + secondDomino
        return totalSum

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The + Operator To An Object To An Integer
    #Parameters: value
    #Return: value + dominoValue
    def __add__(self, value):
        dominoValue = self.value
        if dominoValue // 10 > dominoValue % 10:
            dominoValue = self.flip(dominoValue)
        return value + dominoValue

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The - Operator To Subtract Objects (Values)
    #Parameters: dominoTwo
    #Return: totalDifference
    def __sub__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        totalDifference = firstDomino - secondDomino
        return totalDifference

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The * Operator To Multiply Objects (Values)
    #Parameters: dominoTwo
    #Return: product
    def __mul__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        product = firstDomino * secondDomino
        return product

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The > Operator To Compare Two Objects (Values) And Determine If The First Is Greater Than The Second Object
    #Parameters: dominoTwo
    #Return: answer
    def __gt__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = firstDomino > secondDomino
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The < Operator To Compare Two Objects (Values) And Determine If The First Is Less Than The Second Object
    #Parameters: dominoTwo
    #Return: answer
    def __le__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = firstDomino < secondDomino
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The >= Operator To Compare Two Objects (Values) And Determine If The First Is Greater Than Or Equal To The Second Object
    #Parameters: dominoTwo
    #Return: answer    
    def __ge__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = firstDomino >= secondDomino
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The <= Operator To Compare Two Objects (Values) And Determine If The First Is Less Than Or Equal To The Second Object
    #Parameters: dominoTwo
    #Return: answer
    def __le__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = firstDomino <= secondDomino
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The == Operator To Compare Two Objects (Values) And Determine If The First Is Equal To The Second Object
    #Parameters: dominoTwo
    #Return: answer
    def __eq__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = (firstDomino == secondDomino)
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The == Operator To Compare An Object And Value And Determine If They Are Equal
    #Parameters: dominoTwo
    #Return: answer
    def __eq__(self, value):
        firstDomino = self.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        answer = (firstDomino == value)
        return answer

    #Author: Kavin Muralitharan
    #Date: April 19, 2016
    #Purpose: To Teach The != Operator To Compare Two Objects (Values) And Determine If The First Is Not Equal To The Second Object
    #Parameters: dominoTwo
    #Return: answer
    def __ne__(self, dominoTwo):
        firstDomino = self.value
        secondDomino = dominoTwo.value
        if firstDomino // 10 > firstDomino % 10:
            firstDomino = self.flip(firstDomino)
        if secondDomino // 10 > secondDomino % 10:
            secondDomino = self.flip(secondDomino)
        answer = (firstDomino != secondDomino)
        return answer

#Author: Kavin Muralitharan
#Date: April 29, 2016
#Purpose: To Create A List Of Dominos And Change It Accordingly
#Data Elements:
# size - The Amount Of Dominos
# dominoSize = The Size Of The Dominos
# dominoList - The List That Holds The Dominos
#Methods:
# __str__ - To Make The Domino List Printable (A String)
# valueOfDomino - Returns The Value Of The Given Position's Domino
# sizeOfHand - Returns The Size Of The Hand
# addDomino - Adds Domino To The End Of The List
# setOrientation - Sets The Orientation Of The Dominos
# setFaceUp - Changes Whether A Hand Is Face Up Or Not
# displayHand - Draws The List (Dominos) On The Canvas
# findValue - Returns The Index Of A Given Value In A Hand
# dropDomino - Removes A Domino Depending On A Given Value
# sortHand - Sorts The List Of Dominos
class DominoHand:
    #Author: Kavin Muralitharan
    #Date: April 29, 2016
    #Purpose: To Initialize The Size, DominoSize, and To Create The Domino List
    #Parameters: size and dominoSize
    #Return: None
    def __init__(self, size = 0, dominoSize = 40):
        if str(dominoSize).isdigit() == False or dominoSize < 30 or dominoSize > 72:
            self.dominoSize = 40
        else:
            self.dominoSize = dominoSize
        if str(size).isdigit() == False or size < 0 or size > 7:
            self.size = 4
        else:
            self.size = size
        self.dominoList = []
        for counter in range(self.size):
            self.dominoList.append(Domino(size = self.dominoSize))
            self.dominoList[counter].randomize()

    #Author: Kavin Muralitharan
    #Date: April 29, 2016
    #Purpose: To Make The Domino List Printable (A String)
    #Parameters: None
    #Return: string
    def __str__(self):
        string = "["
        for counter in range(self.size):
            string = string + str(self.dominoList[counter]) + ","
        string = string + "]"
        return string

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Returns The Value Of The Given Position's Domino
    #Parameters: position
    #Return: value
    def valueOfDomino(self, position):
        value = self.dominoList[position].value
        return value

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Returns The Size Of The Hand
    #Parameters: None
    #Return: size
    def sizeOfHand(self):
        size = len(self.dominoList)
        if size != self.size:
            self.size = size
        return size
    
    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Adds Domino To The End Of The List
    #Parameters: dominoValue
    #Return: None
    def addDomino(self, dominoValue = 66):
        if dominoValue // 10 > 6 or dominoValue // 10 < 0 or dominoValue % 10 > 6 or dominoValue % 10 < 6:
            value = 50
        self.dominoList.append(Domino(value = dominoValue, size = 30))
        self.size = self.size + 1

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Sets The Orientation For The Dominos In The List
    #Parameters: orientation
    #Return: None
    def setOrientation(self, orientation = "H"):
        if orientation == "H" or orientation == "V":
            orientation = orientation
        else:
            orientation = "V"
        for counter in range(self.size):
            self.dominoList[counter].setOrientation(orientation)

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Changes Whether A Hand Is Face Up Or Not
    #Parameters: faceUp
    #Return: None
    def setFaceUp(self, faceUp = True):
        if faceUp == True or faceUp == False:
            faceUp = faceUp
        else:
            faceUp = True
        for counter in range(self.size):
            self.dominoList[counter].faceUp = faceUp
            self.dominoList[counter].putFaceUp()

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Draws The List (Dominos) On The Canvas
    #Parameters: canvas, x, & y, place
    #Return: None    
    def displayHand(self, canvas, x = 10, y = 10):
        x2 = x
        y2 = y
        count = 1
        space = 10
        if self.dominoList[0].orientation == "H":
            for counter in range(self.size):
                self.dominoList[counter].draw(canvas, x, y)
                x = x2 + self.dominoList[counter].size * (count * 2) + space
                space = space + 10
                count = count + 1
        if self.dominoList[0].orientation == "V":
            for counter in range(self.size):
                self.dominoList[counter].draw(canvas, x, y)
                y = y2 + self.dominoList[counter].size * (count * 2) + space
                space = space + 10
                count = count + 1

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Returns The Index Of A Given Value In A Hand
    #Parameters: value
    #Return: index
    def findValue(self, value):
        if value in self.dominoList:
            index = self.dominoList.index(value)
        else:
            index = "Not Valid"
        return index

    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Removes A Domino Depending On The Given Value
    #Parameters: value
    #Return: None
    def dropDomino(self, value):
        if value in self.dominoList:
            index = self.dominoList.index(value)
            del self.dominoList[index]
            self.size = self.size - 1
        elif self.dominoList[0].flip(value) in self.dominoList:
            index = self.dominoList.index(self.dominoList[0].flip(value))
            del self.dominoList[index]
            self.size = self.size - 1
            
    #Author: Kavin Muralitharan
    #Date: June 2nd, 2016
    #Purpose: Sorts The Domino Hand
    #Parameters: None
    #Return: None    
    def sortHand(self):
        self.dominoList.sort()

class Table:
    def __init__(self):
        self.tableList = []
    def leftTable(self):
        left = self.tableList[0].value // 10
        return left

    def rightTable(self):
        right = self.tableList[-1].value % 10
        return right

    def drawTable(self, canvas, x, y):
        x2 = x
        y2 = y
        counter = 0
        centerDomino = Domino()
        while centerDomino.value != 66:
            centerDomino = self.tableList[counter]
            counter = counter + 1
        centerDominoPosition = counter - 1
        centerDomino.draw(canvas,x,y)
        leftPosition = centerDominoPosition - 1
        if len(self.tableList[:centerDominoPosition - 1]) >= 4:
            for counter in range(0,4):
                domino = self.tableList[leftPosition]
                leftPosition = leftPosition - 1
                x = x - domino.size * 2 - 5
                domino.draw(canvas, x, y)                
            if len(self.tableList[:centerDominoPosition]) - 4 >= 1:
                domino = self.tableList[leftPosition]
                domino.setOrientation("V")
                leftPosition = leftPosition - 1
                y = y - domino.size * 2 - 5
                domino.draw(canvas, x, y)    
                if len(self.tableList[:centerDominoPosition]) - 5 >= 8:
                    for counter in range(0,8):
                        domino = self.tableList[leftPosition]
                        domino.value = domino.flip(domino.value)
                        domino.setOrientation("H")
                        leftPosition = leftPosition - 1
                        if counter == 0:
                            x = x + domino.size + 5
                        else:
                            x = x + domino.size * 2 + 5
                        domino.draw(canvas, x, y)
                        domino.value = domino.flip(domino.value)
                    if len(self.tableList[:centerDominoPosition]) - 13 >= 1:
                        domino = self.tableList[leftPosition]
                        domino.setOrientation("V")
                        leftPosition = leftPosition - 1
                        x = x + domino.size
                        y = y - domino.size * 2 - 5
                        domino.draw(canvas, x, y)
                        if len(self.tableList[:centerDominoPosition]) - 14 >= 8:
                            for counter in range(0,8):
                                domino = self.tableList[leftPosition]
                                domino.setOrientation("H")
                                leftPosition = leftPosition - 1
                                x = x - domino.size * 2 - 5
                                domino.draw(canvas, x, y)
                            if len(self.tableList[:centerDominoPosition]) - 22 >= 1:
                                domino = self.tableList[leftPosition]
                                domino.setOrientation("V")
                                leftPosition = leftPosition - 1
                                y = y - domino.size * 2 - 5
                                domino.draw(canvas, x, y)
                                if len(self.tableList[:centerDominoPosition]) - 23 >= 1:
                                    for counter in range(len(self.tableList[:centerDominoPosition]) - 23):
                                        domino = self.tableList[leftPosition]
                                        domino.setOrientation("H")
                                        leftPosition = leftPosition - 1
                                        if counter == 0:
                                            x = x + domino.size + 5
                                        else:
                                            x = x + domino.size * 2 + 5
                                        domino.draw(canvas, x, y)
                        else:
                            for counter in range(len(self.tableList[:centerDominoPosition]) - 14):
                                domino = self.tableList[leftPosition]
                                domino.setOrientation("H")
                                leftPosition = leftPosition - 1
                                x = x - domino.size * 2 - 5
                                domino.draw(canvas, x, y)
                else:
                    for counter in range(len(self.tableList[:centerDominoPosition]) - 5):
                        domino = self.tableList[leftPosition]
                        domino.value = domino.flip(domino.value)
                        domino.setOrientation("H")
                        leftPosition = leftPosition - 1
                        if counter == 0:
                            x = x + domino.size + 5
                        else:
                            x = x + domino.size * 2 + 5
                        domino.draw(canvas, x, y)
                        domino.value = domino.flip(domino.value)
        else:
            for counter in range(0, len(self.tableList[:centerDominoPosition])):
                domino = self.tableList[leftPosition]
                leftPosition = leftPosition - 1
                x = x - domino.size * 2 - 5
                domino.draw(canvas, x, y)
        x = x2
        y = y2
        rightPosition = centerDominoPosition + 1
        if len(self.tableList[centerDominoPosition + 1:]) >= 4:
            for counter in range(0,4):
                domino = self.tableList[rightPosition]
                rightPosition = rightPosition + 1
                x = x + domino.size * 2 + 5
                domino.draw(canvas, x, y)                
            if len(self.tableList[centerDominoPosition + 1:]) - 4 >= 1:
                domino = self.tableList[rightPosition]
                domino.setOrientation("V")
                rightPosition = rightPosition + 1
                x = x + domino.size
                y = y + domino.size + 5
                domino.draw(canvas, x, y)
                x = x - domino.size
                y = y + domino.size
                if len(self.tableList[centerDominoPosition + 1:]) - 5 >= 8:
                    for counter in range(0,8):
                        domino = self.tableList[rightPosition]
                        domino.value = domino.flip(domino.value)
                        domino.setOrientation("H")
                        rightPosition = rightPosition + 1
                        if counter == 0:
                            x = x - domino.size - 5
                        else:
                            x = x - domino.size * 2 - 5
                        domino.draw(canvas, x, y)
                        domino.value = domino.flip(domino.value)
                    if len(self.tableList[centerDominoPosition + 1:]) - 13 >= 1:
                        domino = self.tableList[rightPosition]
                        domino.setOrientation("V")
                        rightPosition = rightPosition + 1
                        y = y + domino.size + 5
                        domino.draw(canvas, x, y)
                        y = y + domino.size
                        if len(self.tableList[centerDominoPosition + 1:]) - 14 >= 8:
                            for counter in range(0,8):
                                domino = self.tableList[rightPosition]
                                domino.setOrientation("H")
                                rightPosition = rightPosition + 1
                                if counter == 0:
                                    x = x + domino.size + 5
                                else:
                                    x = x + domino.size * 2 + 5
                                domino.draw(canvas, x, y)
                            if len(self.tableList[centerDominoPosition + 1:]) - 22 >= 1:
                                domino = self.tableList[rightPosition]
                                domino.setOrientation("V")
                                rightPosition = rightPosition - 1
                                y = y + domino.size + 5
                                x = x + domino.size
                                domino.draw(canvas, x, y)
                                if len(self.tableList[centerDominoPosition + 1:]) - 23 >= 1:
                                    y = y + domino.size
                                    for counter in range(len(self.tableList[centerDominoPosition + 1:]) - 23):
                                        domino = self.tableList[rightPosition]
                                        domino.setOrientation("H")
                                        rightPosition = rightPosition - 1
                                        x = x - domino.size * 2 - 5
                                        domino.draw(canvas, x, y)
                        else:
                            for counter in range(len(self.tableList[centerDominoPosition + 1:]) - 14):
                                domino = self.tableList[rightPosition]
                                domino.setOrientation("H")
                                rightPosition = rightPosition + 1
                                if counter == 0:
                                    x = x + domino.size + 5
                                else:
                                    x = x + domino.size * 2 + 5
                                domino.draw(canvas, x, y)
                else:
                    for counter in range(len(self.tableList[centerDominoPosition + 1:]) - 5):
                        domino = self.tableList[rightPosition]
                        domino.value = domino.flip(domino.value)
                        domino.setOrientation("H")
                        rightPosition = rightPosition + 1
                        if counter == 0:
                            x = x - domino.size - 5
                        else:
                            x = x - domino.size * 2 - 5
                        domino.draw(canvas, x, y)
                        domino.value = domino.flip(domino.value)
        else:
            for counter in range(0, len(self.tableList[centerDominoPosition + 1:])):
                domino = self.tableList[rightPosition]
                rightPosition = rightPosition + 1
                x = x + domino.size * 2 + 5
                domino.draw(canvas, x, y)
        
    def addToTable(self, value, position = "right"):
        if position == "right":
            rightDomino = Domino(value = value, size = 30)
            self.tableList.append(rightDomino)
        elif position == "left":
            leftDomino = Domino(value = value, size = 30)
            self.tableList.insert(0,leftDomino)
        for counter in range(len(self.tableList)):
            print(self.tableList[counter], end = " ")
        print()


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
    def __init__(self):
        self.available = []
        self.hands = []
        for counter in range(4):
            self.hands.append(DominoHand(size = 7, dominoSize = 30))
            hand = self.hands[counter]
            for counter in range(7):
                while hand.valueOfDomino(counter) in self.available or int(str(hand.valueOfDomino(counter))[::-1]) in self.available or hand.valueOfDomino(counter) * 10 in self.available:
                    hand.dominoList[counter].randomize()
                self.available.append(hand.valueOfDomino(counter))
                hand.dominoList[counter].faceUpValue = hand.dominoList[counter].value
        self.table = Table()
        self.names = []
        self.currentPlayer = 0
        self.labelNames = []
    def setup(self, canvas, canvasTwo):
        self.getNames()
        name1 = Label(canvas, text = self.names[0], fg = "#F1F0FF", bg = "#4b0066", font = ("Oratar Std", 13, "bold"))
        name1.place(x = 400, y = 645)
        self.labelNames.append(name1)
        name2 = Label(canvas, text = self.names[1], fg = "#F1F0FF", bg = "#4b0066", font = ("Oratar Std", 13, "bold"))
        name2.place(x = 790, y = 80)
        self.labelNames.append(name2)
        name3 = Label(canvas, text = self.names[2], fg = "#F1F0FF", bg = "#4b0066", font = ("Oratar Std", 13, "bold"))
        name3.place(x = 400, y = 45)
        self.labelNames.append(name3)
        name4 = Label(canvas, text = self.names[3], fg = "#F1F0FF", bg = "#4b0066", font = ("Oratar Std", 13, "bold"))
        name4.place(x = 10, y = 80)
        self.labelNames.append(name4)
        
        firstPlayer = self.firstMove()
        tempOne = self.hands.pop(firstPlayer)
        self.hands.append(tempOne)
        firstPlayerHand = self.hands[3]
        
        index = firstPlayerHand.findValue(value = 66)
        self.table.tableList.append(firstPlayerHand.dominoList[index])
        self.table.tableList[0].setOrientation("H")
        self.table.drawTable(canvasTwo, x = 295, y = 225)
        self.hands[3].dropDomino(value = 66)
        canvas.delete("all")
        for counter in range(len(self.hands)):
            if counter == 0:
                self.hands[counter].setFaceUp(faceUp = True)
            else:
                self.hands[counter].setFaceUp(faceUp = False)
        self.deal(canvas)
    def getNames(self):
        playerSum = option1.get() + option2.get() + option3.get() + option4.get()
        if playerSum == 1:
            self.names.append(player1.get()[:9])
            self.names.append("Computer #1")
            self.names.append("Computer #2")
            self.names.append("Computer #3")
        elif playerSum == 2:
            self.names.append(player1.get()[:9])
            self.names.append(player2.get()[:9])
            self.names.append("Computer #1")
            self.names.append("Computer #2")
        elif playerSum == 3:
            self.names.append(player1.get()[:9])
            self.names.append(player2.get()[:9])
            self.names.append(player3.get()[:9])
            self.names.append("Computer #1")
        elif playerSum == 4:
            self.names.append(player1.get()[:9])
            self.names.append(player2.get()[:9])
            self.names.append(player3.get()[:9])
            self.names.append(player4.get()[:9])

    def deal(self, canvas):
        for counter in range(len(self.hands)):
            if counter == 0:
                self.hands[counter].displayHand(canvas, x = 215, y = 610)
            elif counter == 1:
                self.hands[counter].setOrientation(orientation = "V")
                self.hands[counter].displayHand(canvas, x = 820, y = 115)
            elif counter == 2:
                self.hands[counter].setOrientation(orientation = "H")
                self.hands[counter].displayHand(canvas, x = 215, y = 75)
            else:
                self.hands[counter].setOrientation(orientation = "V")
                self.hands[counter].displayHand(canvas, x = 45, y = 115)

    def updateHands(self, canvas, currentHand):
        canvas.delete("all")
        self.hands[currentHand].setOrientation("H")
        self.hands[currentHand].setFaceUp(True)
        self.hands[currentHand].displayHand(canvas, x = 215, y = 610)
        print(self.labelNames[currentHand])
        self.labelNames[currentHand].place(x = 400, y = 645)
        for counter in range(len(self.hands)):
            if counter == currentHand:
                self.hands[counter].setFaceUp(faceUp = True)
            else:
                self.hands[counter].setFaceUp(faceUp = False)
        if currentHand == 0:
            self.hands[1].setOrientation(orientation = "V")
            self.hands[1].displayHand(canvas, x = 820, y = 115)
            self.labelNames[1].place(x = 790, y = 80)
            self.hands[2].setOrientation(orientation = "H")
            self.hands[2].displayHand(canvas, x = 215, y = 75)
            self.labelNames[2].place(x = 400, y = 45)
            self.hands[3].setOrientation(orientation = "V")
            self.hands[3].displayHand(canvas, x = 45, y = 115)
            self.labelNames[3].place(x = 10, y = 80)
        elif currentHand == 1:
            self.hands[2].setOrientation(orientation = "V")
            self.hands[2].displayHand(canvas, x = 820, y = 115)
            self.labelNames[2].place(x = 790, y = 80)
            self.hands[3].setOrientation(orientation = "H")
            self.hands[3].displayHand(canvas, x = 215, y = 75)
            self.labelNames[3].place(x = 400, y = 45)
            self.hands[0].setOrientation(orientation = "V")
            self.hands[0].displayHand(canvas, x = 45, y = 115)
            self.labelNames[0].place(x = 10, y = 80)
        elif currentHand == 2:
            self.hands[3].setOrientation(orientation = "V")
            self.hands[3].displayHand(canvas, x = 820, y = 115)
            self.labelNames[3].place(x = 790, y = 80)
            self.hands[0].setOrientation(orientation = "H")
            self.hands[0].displayHand(canvas, x = 215, y = 75)
            self.labelNames[0].place(x = 400, y = 45)
            self.hands[1].setOrientation(orientation = "V")
            self.hands[1].displayHand(canvas, x = 45, y = 115)
            self.labelNames[1].place(x = 10, y = 80)
        else:
            self.hands[0].setOrientation(orientation = "V")
            self.hands[0].displayHand(canvas, x = 820, y = 115)
            self.labelNames[0].place(x = 790, y = 80)
            self.hands[1].setOrientation(orientation = "H")
            self.hands[1].displayHand(canvas, x = 215, y = 75)
            self.labelNames[1].place(x = 400, y = 45)
            self.hands[2].setOrientation(orientation = "V")
            self.hands[2].displayHand(canvas, x = 45, y = 115)
            self.labelNames[2].place(x = 10, y = 80)
    
    def canMove(self, playerHand):
        rightSide = self.table.rightTable()
        leftSide = self.table.leftTable()
        hand = self.hands[playerHand]
        canMove = False
        for counter in range(len(hand.dominoList)):
            if hand.valueOfDomino(counter) % 10 == rightSide or hand.valueOfDomino(counter) % 10 == leftSide:
                canMove = True
                break
            elif hand.valueOfDomino(counter) // 10 == rightSide or hand.valueOfDomino(counter) // 10 == leftSide:
                canMove = True
                break
            else:
                canMove = False
        return canMove

    def firstMove(self):
        for counter in range(len(self.hands)):
            if 66 in self.hands[counter].dominoList:
                player = counter
        return player

    def getUsersMove(self, intUsersHand):
        rightSide = self.table.rightTable()
        leftSide = self.table.leftTable()
        moved = False
        usersHand = self.hands[intUsersHand]
        xValue = xValueClick.get()
        yValue = yValueClick.get()
        leftValue = intLeftValue.get()
        rightValue = intRightValue.get()
        if xValue >= 214 and xValue <= 275 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 1:
            domino = usersHand.dominoList[0]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
        elif xValue >= 284 and xValue <= 345 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 2:
            domino = usersHand.dominoList[1]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
        elif xValue >= 354 and xValue <= 415 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 3:
            domino = usersHand.dominoList[2]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved == False
        elif xValue >= 424 and xValue <= 485 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 4:
            domino = usersHand.dominoList[3]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
        elif xValue >= 494 and xValue <= 555 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 5:
            domino = usersHand.dominoList[4]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
        elif xValue >= 564 and xValue <= 625 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) >= 6:
            domino = usersHand.dominoList[5]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
        elif xValue >= 634 and xValue <= 695 and yValue >= 610 and yValue <= 640 and len(usersHand.dominoList) == 7:
            domino = usersHand.dominoList[6]
            if leftValue == 1:
                if domino.value % 10 == leftSide:
                    self.table.addToTable(domino.value, "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == leftSide:
                    self.table.addToTable(domino.flip(domino.value), "left")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            elif rightValue == 1:
                if domino.value % 10 == rightSide:
                    self.table.addToTable(domino.flip(domino.value), "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                elif domino.value // 10 == rightSide:
                    self.table.addToTable(domino.value, "right")
                    self.hands[intUsersHand].dropDomino(domino.value)
                    moved = True
                else:
                    moved = False
            
        return moved

    
    def getComputersMove(self, computerHand):
        canMove = self.canMove(computerHand)
        moved = False
        hand = self.hands[computerHand]
        if canMove == True:
            rightSide = self.table.rightTable()
            leftSide = self.table.leftTable()
            counter = 0
            while counter < len(hand.dominoList) and moved == False:
                if hand.valueOfDomino(counter) % 10 == rightSide:
                    dominoValue = hand.valueOfDomino(counter)
                    self.table.addToTable(value = hand.dominoList[counter].flip(dominoValue), position = "right")
                    hand.dropDomino(value = hand.valueOfDomino(counter))
                    moved = True
                elif hand.valueOfDomino(counter) // 10 == rightSide:
                    dominoValue = hand.valueOfDomino(counter)
                    self.table.addToTable(value = dominoValue, position = "right")
                    hand.dropDomino(value = dominoValue)
                    moved = True
                elif hand.valueOfDomino(counter) % 10 == leftSide:
                    dominoValue = hand.valueOfDomino(counter)
                    self.table.addToTable(value = dominoValue, position = "left")
                    hand.dropDomino(value = dominoValue)
                    moved = True
                elif hand.valueOfDomino(counter) // 10 == leftSide:
                    dominoValue = hand.valueOfDomino(counter)
                    self.table.addToTable(value = hand.dominoList[counter].flip(dominoValue), position = "left")
                    hand.dropDomino(value = hand.valueOfDomino(counter))
                    moved = True
                counter = counter + 1
            return canMove
        
    def play(self, canvasOne, canvasTwo):
        self.setup(canvasOne, canvasTwo)
            
    def popUpMessage(self, option):
        if option == 1:
            messagebox.showinfo("First Move", "Computer #3 Finished His First Move")
        elif option == 2:
            messagebox.showwarning("Invalid", "Invalid Move! Please Try Again")
        elif option == 3:
            messagebox.showinfo("Move Made", str(self.names[self.currentPlayer]) + " has just made his move!")
        elif option == 4:
            name = self.names[self.currentPlayer]
            if name[:8] != "Computer":
                name = "You"
            messagebox.showinfo("Pass", name + " cannot move! A Pass was made")
        elif option == 5:
            messagebox.showinfo("Winner!", self.names[self.currentPlayer] + " wins the game!")
        elif option == 6:
            messagebox.showinfo("Player Turn", "It is " + self.names[self.currentPlayer] + " turn")
#Sub-Programs
def showForm(form):
    form.deiconify()

def startGame(form, menuForm, kala, canvasOne, canvasTwo):
    showForm(form)
    menuForm.destroy()
    kala.play(canvasOne, canvasTwo)
    kala.popUpMessage(1)
    
def mouseClick(event):
    gameOver = False
    computerMove = True
    name = kala.names[kala.currentPlayer]
    if name[:8] != "Computer":
        kala.popUpMessage(6)
        kala.hands[kala.currentPlayer].setOrientation("H")
        kala.hands[kala.currentPlayer].setFaceUp(faceUp = True)
        if kala.canMove(kala.currentPlayer) == False:
            kala.popUpMessage(4)
            computerMove = False
            if kala.currentPlayer == 3:
                kala.currentPlayer = 0
            else:
                kala.currentPlayer = kala.currentPlayer + 1
        else:
            xValueClick.set(event.x)
            yValueClick.set(event.y)
            moved = kala.getUsersMove(kala.currentPlayer)
            if moved == True:
                canvasTwo.delete("all")
                kala.table.drawTable(canvasTwo, 295, 225)
                if kala.hands[kala.currentPlayer].sizeOfHand() == 0:
                    kala.popUpMessage(5)
                    form.destroy()
                    gameOver = True
                else:
                    if kala.currentPlayer == 3:
                        kala.currentPlayer = 0
                    else:
                        kala.currentPlayer = kala.currentPlayer + 1
                    computerMove = False
            else:
                kala.popUpMessage(2)
    if gameOver == False:     
        while computerMove == False:
            name = kala.names[kala.currentPlayer]
            while name[:8] == "Computer":
                kala.hands[kala.currentPlayer].setFaceUp(True)
                if kala.canMove(kala.currentPlayer) == True:
                    kala.getComputersMove(kala.currentPlayer)
                    canvasTwo.delete("all")
                    kala.table.drawTable(canvasTwo, 295, 225)
                    kala.popUpMessage(3)
                    if kala.hands[kala.currentPlayer].sizeOfHand() == 0:
                        kala.popUpMessage(5)
                        form.destroy()
                        gameOver = True
                        computerMove = True
                    else:
                        if kala.currentPlayer == 3:
                            kala.currentPlayer = 0
                        else:
                            kala.currentPlayer = kala.currentPlayer + 1
                        name = kala.names[kala.currentPlayer]
                else:
                    if gameOver == False:
                        kala.popUpMessage(4)
                        if kala.currentPlayer == 3:
                            kala.currentPlayer = 0
                        else:
                            kala.currentPlayer = kala.currentPlayer + 1
                        name = kala.names[kala.currentPlayer]
            computerMove = True
        if gameOver == False:
            kala.updateHands(canvasOne, kala.currentPlayer)


def rightButtonClick():
    intRightValue.set(1)
    intLeftValue.set(0)

def leftButtonClick():
    intLeftValue.set(1)
    intRightValue.set(0)

def enableDisable(player):
    if player == 1:
        player1Option.select()
        if option1.get() == 1:
            player1Name.configure(state="normal")
            player2Option.configure(state="normal")
        else:
            player1Name.configure(state="disabled")
            player2Option.configure(state="normal")
            player2Name.configure(state="disabled")
            player3Option.configure(state="disabled")
            player4Option.configure(state="disabled")
            player4Name.configure(state="disabled")
            player3Name.configure(state="disabled")
            if option2.get() == 1:
                player2Option.deselect()
            if option3.get() == 1:
                player3Option.deselect()
            if option4.get() == 1:
                player4Option.deselect()
            
    if player == 2:    
        if option2.get() == 1:
            player2Name.configure(state="normal")
            player3Option.configure(state="normal")
        else:
            player2Name.configure(state="disabled")
            player3Option.configure(state="disabled")
            player4Option.configure(state="disabled")
            player4Name.configure(state="disabled")
            player3Name.configure(state="disabled")
            if option3.get() == 1:
                player3Option.deselect()
            if option4.get() == 1:
                player4Option.deselect()
            
    if player == 3:
        if option3.get() == 1:
            player3Name.configure(state="normal")
            player4Option.configure(state="normal")
        else:
            player3Name.configure(state="disabled")
            player4Option.configure(state="disabled")
            if option4.get() == 1:
                player4Option.deselect()
                
    if player == 4:
        if option4.get() == 1:
            player4Name.configure(state="normal")
        else:
            player4Name.configure(state="disabled")

#Main Program

textColour = "#F1F0FF"
backgroundColour = "#4b0066"
foregroundColour = "#9900CC"
#Main-Menu Form (Root)
menuForm = Tk()
menuForm.title("Main Menu!")
menuForm.config(width = 400, height = 400, background = backgroundColour)
menuForm.minsize(width = 400, height = 400)
menuForm.maxsize(width = 400, height = 400)

titleLabelMenu = Label(menuForm, text = "KALAMINOES!", font = ("Oratar Std", 25, "bold"), bg = backgroundColour, fg = textColour)

option1 = IntVar()
option2 = IntVar()
option3 = IntVar()
option4 = IntVar()

startButton = Button(menuForm, text = "Start Game", width = 10, height = 1, font = ("Oratar Std", 20, "bold"), bg = foregroundColour, fg = textColour, command = lambda:startGame(form, menuForm, kala, canvasOne, canvasTwo))
player1Option = Checkbutton(menuForm, text = "Player 1", variable = option1, font = ("Oratar Std", 14, "bold"), bg = backgroundColour, fg = textColour, selectcolor = foregroundColour, command = lambda:enableDisable(1))
player2Option = Checkbutton(menuForm, text = "Player 2", variable = option2, font = ("Oratar Std", 14, "bold"), bg = backgroundColour, fg = textColour, selectcolor = foregroundColour, command = lambda:enableDisable(2))
player3Option = Checkbutton(menuForm, text = "Player 3", variable = option3, font = ("Oratar Std", 14, "bold"), bg = backgroundColour, fg = textColour, selectcolor = foregroundColour, command = lambda:enableDisable(3))
player4Option = Checkbutton(menuForm, text = "Player 4", variable = option4, font = ("Oratar Std", 14, "bold"), bg = backgroundColour, fg = textColour, selectcolor = foregroundColour, command = lambda:enableDisable(4))
player1Option.select()

player1 = StringVar()
player2 = StringVar()
player3 = StringVar()
player4 = StringVar()

player1Name = Entry(menuForm, width = 25, bg = foregroundColour, fg = textColour, font = ("Oratar Std", 11, "bold"), textvariable = player1)
player2Name = Entry(menuForm, width = 25, bg = foregroundColour, fg = textColour, font = ("Oratar Std", 11, "bold"), textvariable = player2)
player3Name = Entry(menuForm, width = 25, bg = foregroundColour, fg = textColour, font = ("Oratar Std", 11, "bold"), textvariable = player3)
player4Name = Entry(menuForm, width = 25, bg = foregroundColour, fg = textColour, font = ("Oratar Std", 11, "bold"), textvariable = player4)

player2Name.configure(state="disabled")
player3Name.configure(state="disabled")
player4Name.configure(state="disabled")

player3Option.configure(state="disabled") 
player4Option.configure(state="disabled")

#Positioning Widgets
titleLabelMenu.place(x = 83, y = 5)
startButton.place(x = 110, y = 300)
player1Option.place (x = 20, y = 80)
player2Option.place (x = 20, y = 130)
player3Option.place (x = 20, y = 180)
player4Option.place (x = 20, y = 230)
player1Name.place(x = 170, y = 85)
player2Name.place(x = 170, y = 135)
player3Name.place(x = 170, y = 185)
player4Name.place(x = 170, y = 235)

#Game Form (Root)
form = Tk()

form.title("KALAMINOES!")
form.config(width = 900, height = 700)
form.minsize(width = 900, height = 700)
form.maxsize(width = 900, height = 700)

xValueClick = IntVar()
yValueClick = IntVar()

canvasOne = Canvas(form, width = 900, height = 700)
canvasOne.config(bg = backgroundColour)

canvasTwo = Canvas(form, width = 650, height = 480)
canvasTwo.config(bg = foregroundColour)

titleLabel = Label(canvasOne, text = "KALAMINOES!", font = ("Oratar Std", 25, "bold"), bg = backgroundColour, fg = textColour)

intLeftValue = IntVar()
intRightValue = IntVar()

leftButton = Button(canvasOne, text = "Left", width = 15, height = 2, bg = "#8307C2", font = ("Oratar Std", 14, "bold"), command = lambda:leftButtonClick())
rightButton = Button(canvasOne, text = "Right", width = 15, height = 2, bg = "#8307C2", font = ("Oratar Std", 14, "bold"), command = lambda:rightButtonClick())

canvasOne.bind("<Button-1>", mouseClick)

#Positioning Widgets
canvasOne.place(x = 0, y = 0)
canvasTwo.place(x = 125, y = 115)
leftButton.place(x = 20, y = 620)
rightButton.place(x = 700, y = 620)
titleLabel.place(x = 330, y = 5)

form.withdraw()

kala = DominoGame()
form.mainloop()
