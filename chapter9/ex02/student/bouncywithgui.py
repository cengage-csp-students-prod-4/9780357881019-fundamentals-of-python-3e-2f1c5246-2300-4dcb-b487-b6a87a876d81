"""
program: bouncywithgui.py
Author: Michael Guillen

Present a GUI window that computes ball's bounciness
"""

from breezypythongui import EasyFrame

class BounceCalculator(EasyFrame):
    """window that asks user for initial height of ball bounce, bounciness index, and # of bounces,
    calculates the total distance it traveled"""

    def __init__(self):
        EasyFrame.__init__(self, "Bouncy", width = 350, height = 200)

        # add labels
        self.addLabel("Initial height", row = 0, column = 0,
                      sticky = "W")
        self.addLabel("Bounciness index", row = 1, column = 0,
                      sticky = "W")
        self.addLabel("Number of bounces", row = 2, column = 0,
                      sticky = "W")
        self.addLabel("Total distance", 4, 0,
                              sticky = "W")

        # add input and display fields
        self.intHeight = self.addFloatField(0.0, row = 0, column = 1)
        self.bncIndx = self.addFloatField(value = 0.0, row = 1, column = 1)
        self.numBounces = self.addIntegerField(value = 0, row = 2, column = 1)
        self.answerDisplay = self.addFloatField(0.0, 4, 1,
                                    state = "readonly")

        # add button to calculate
        self.addButton("Compute", 3, 1,
                       command = self.calculator)

        

    def calculator(self):
        """Calculate the distance of a ball using its drop height,
        bounce index, and number of bounces"""
        dropHeight = self.intHeight.getNumber()
        bnceIndx = self.bncIndx.getNumber()
        numOfBncs = self.numBounces.getNumber()
        totDist = dropHeight
        curDist = dropHeight*bnceIndx

        for x in range(1, numOfBncs+1):
            if x == 1: # checking if its the first bounce
                totDist = totDist + curDist
            else:
                prevDist = curDist
                curDist = curDist*bnceIndx
                totDist = totDist + prevDist + curDist

        self.answerDisplay.setNumber(totDist)

def main():
    BounceCalculator().mainloop()

if __name__ == "__main__":
    main()