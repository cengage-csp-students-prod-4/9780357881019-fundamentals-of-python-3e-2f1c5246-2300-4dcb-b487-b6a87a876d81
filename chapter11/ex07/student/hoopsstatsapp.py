"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd


def cleanColumn(frame, columnName):
    """Separates a single, combined column, into two neat ones"""
    poppedCol = frame.pop(columnName)
    makes = []
    attempts = []
    for val in poppedCol:
        makes.append(int(val.split("-")[0]))
        attempts.append(int(val.split("-")[1]))
    newPos = frame.columns.get_loc("FG%")
    frame.insert(newPos, columnName + "A", attempts)
    frame.insert(newPos, columnName + "M", makes)


def cleanStats(frame):
    """Takes in a data frame and outputs the same data frame
    with clean columns"""
    cleanColumn(frame, "FG")
    cleanColumn(frame, "3PT")
    cleanColumn(frame, "FT")
    return frame


def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    HoopStatsView(cleanStats(frame)).mainloop()


if __name__ == "__main__":
    main()
