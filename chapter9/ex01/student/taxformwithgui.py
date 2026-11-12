"""
program: taxformwithgui.py
Author: Michael Guillen

Present a GUI window that computes a person's income tax
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Tax Calculator")
        
        self.addLabel("Gross income", 0, 0)
        self.grossIncome = self.addFloatField(0.0, 0, 1, 
                                                precision = 2)
        
        self.addLabel("Dependents", 1, 0)
        self.numDependents = self.addIntegerField(0, 1, 1)

        self.addButton("Compute", 2, 1,
                       command = self.calculator)

        self.addLabel("Total tax", 3, 0)
        self.answerDisplay = self.addFloatField(0.0, 3, 1, 
                                    precision = 2, state = "readonly")

    def calculator(self):
        TAX_RATE = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0

        taxableIncome = self.grossIncome.getNumber() - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * self.numDependents.getNumber()
        incomeTax = taxableIncome * TAX_RATE

        self.answerDisplay.setNumber(incomeTax)

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()