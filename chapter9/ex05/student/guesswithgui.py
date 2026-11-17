"""
Program: guesswithgui.py
Author: Michael Guillen

A GUI program with the ability to guess what number the
user is thinking of by narrowing the number via user input
"""

from breezypythongui import EasyFrame
import random


class GuessingGame(EasyFrame):
    """GUI base game that guesses a number from the user
    whether the number is too small, too large, or correct"""

    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game", resizable = False)

        # label where the computer shows the guess number
        self.guessLabel = self.addLabel(
            text = 'Click "New game" to start!',
            row = 0,
            column = 0,
            columnspan = 4,
            sticky = "NSEW",
        )

        # buttons
        self.smallBtn = self.addButton(
            text = "Too small",
            row = 1,
            column = 0,
            command = self.tooSmallCmd,
            state = "disabled"
        )
        self.largeBtn = self.addButton(
            text = "Too large",
            row = 1,
            column = 1,
            command = self.tooLargeCmd,
            state = "disabled"
        )
        self.correctBtn = self.addButton(
            text = "Correct",
            row = 1,
            column = 2,
            command = self.endGame,
            state = "disabled"
        )
        self.newGameBtn = self.addButton(
            text = "New game",
            row = 1,
            column = 3,
            command = self.newGameCmd
        )
        self.hintBtns = [self.smallBtn, self.largeBtn, self.correctBtn]

    # command methods for buttons
    def newGameCmd(self):
        self.computerGuess = random.randint(1, 100)  # will be called first
        self.smaller = 1
        self.larger = 100
        self.setGuess(self.computerGuess)
        self.newGameBtn["state"] = "disabled"
        for btn in self.hintBtns:
            btn["state"] = "normal"

    def tooSmallCmd(self):
        self.smaller = self.computerGuess + 1
        if self.cheatChecker():
            return
        self.computerGuess = random.randint(self.smaller, self.larger)
        self.setGuess(self.computerGuess)

    def tooLargeCmd(self):
        self.larger = self.computerGuess - 1
        if self.cheatChecker():
            return
        self.computerGuess = random.randint(self.smaller, self.larger)
        self.setGuess(self.computerGuess)

    def endGame(self):
        self.messageBox(
            title = "Game over!",
            message = "Correct guess: " + str(self.computerGuess)
        )
        for btn in self.hintBtns:
            btn["state"] = "disabled"
        self.newGameBtn["state"] = "normal"
        self.guessLabel["text"] = 'Click "New game" to start!'

    def setGuess(self, number):
        self.guessLabel["text"] = "Is the number " + str(number) + "?"

    def cheatChecker(self):
        if self.smaller > self.larger:
            self.messageBox(
                title = "Booo!",
                message = "You lied and cheated >:("
            )
            self.endGame()
            return True
        else:
            return False


def main():
    GuessingGame().mainloop()


if __name__ == "__main__":
    main()
