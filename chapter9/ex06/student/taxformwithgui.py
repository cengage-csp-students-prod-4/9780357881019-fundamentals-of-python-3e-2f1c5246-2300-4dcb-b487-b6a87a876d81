"""
program: taxformwithgui.py
Author: Michael Guillen

Present a GUI window that computes a person's income tax
"""

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Tax Calculator")

        self.addLabel("Income", 0, 0)
        self.grossIncome = self.addFloatField(0.0, 0, 1,
                                              precision = 2)

        self.addLabel("Dependents", 1, 0)
        self.numDependents = self.addIntegerField(0, 1, 1)

        self.addButton("Compute", 2, 1,
                       command = self.calculator)

        self.addLabel("Total tax", 3, 0)
        self.answerDisplay = self.addFloatField(0.0, 3, 1,
                                                precision = 2, state = "readonly")

        self.statusGroup = self.addRadiobuttonGroup(
            row = 0,
            column = 2,
            rowspan = 3,
        )
        single = self.statusGroup.addRadiobutton(text = "Single")
        self.statusGroup.addRadiobutton(text = "Married")
        self.statusGroup.addRadiobutton(text = "Divorced")
        self.statusGroup.setSelectedButton(single)

    def calculator(self):
        status = self.statusGroup.getSelectedButton()["text"]
        if status == "Divorced":
            taxRate = 0.10
        elif status == "Married":
            taxRate = 0.15
        else:
            taxRate = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0

        taxableIncome = self.grossIncome.getNumber() - STANDARD_DEDUCTION - \
            DEPENDENT_DEDUCTION * self.numDependents.getNumber()
        incomeTax = taxableIncome * taxRate

        self.answerDisplay.setNumber(incomeTax)


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
