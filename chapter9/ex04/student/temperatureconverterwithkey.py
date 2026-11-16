from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):
    """Converts degrees from Fahrenheit to Celsius
    and vice-versa"""

    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        # add labels
        self.addLabel(text="Celsius", row=0, column=0)
        self.addLabel(text="Fahrenheit", row=0, column=1)

        # add input fields
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=0, precision=1)
        self.fahrenheitField = self.addFloatField(
            value=32.0, row=1, column=1, precision=1
        )

        # add buttons/keybinds
        self.addButton(text=">>>>", row=2, column=0, command=self.celToFahren)
        self.celsiusField.bind("<Return>", lambda event: self.celToFahren())

        self.addButton(text="<<<<", row=2, column=1, command=self.fahrenToCel)
        self.fahrenheitField.bind("<Return>", lambda event: self.fahrenToCel())

    def celToFahren(self):
        """convert degrees in Celsius to Fahrenheit"""

        degreesC = self.celsiusField.getNumber()
        degreesF = (degreesC * (9 / 5)) + 32

        self.fahrenheitField.setNumber(degreesF)

    def fahrenToCel(self):
        """convert degrees in Fahrenheit to Celsius"""

        degreesF = self.fahrenheitField.getNumber()
        degreesC = (degreesF - 32) * (5 / 9)

        self.celsiusField.setNumber(degreesC)


def main():
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()
