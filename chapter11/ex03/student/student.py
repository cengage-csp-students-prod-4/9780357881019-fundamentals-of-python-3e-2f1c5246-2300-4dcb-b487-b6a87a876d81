""" 
File: student.py
Author: Michael Guillen

model for creating a table with information
on a given student's scores
"""

import stats
import numpy as np


class Student(object):
    """Creates and returns a tabel for a student's scores,
    mean, median, mode, and standard deviation"""

    def __init__(self, name, number):
        """Creates the initial table and variable"""

        self.name = name
        self.scores = []
        for _ in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the name of the student"""
        return self.name

    def numScores(self):
        """Returns the amount of scores in the list"""
        return len(self.scores)

    def getScore(self, i):
        """Returns the specific score at position i"""
        return self.scores[i - 1]

    def setScore(self, i, score):
        """Sets a custom score to position i"""
        self.scores[i - 1] = score

    def addScore(self, score):
        """Adds a custom score to the end of the list"""
        self.scores.append(score)

    def deleteScore(self, i):
        """Deletes a specific score at position i"""
        self.scores.pop(i - 1)

    def randomizeScores(self, size, lower, upper):
        """Wipes the current list and creates a 
        size amount of scores ranging from lower to upper"""
        self.scores = stats.getRandomList(size, lower, upper)

    def getMean(self):
        """Returns the mean of the scores"""
        return np.mean(self.scores)

    def getMedian(self):
        """Returns the median of the scores"""
        return np.median(self.scores)

    def getStd(self):
        """Returns the standard deviation of the scores"""
        return np.std(self.scores)

    def getMode(self):
        """Returns the mode of the scores"""
        return stats.mode(self.scores)

    def __str__(self):
        """Creates and returns an organized list with
        all the information of the table"""
        result = "Position Score\n"
        i = 1
        for score in self.scores:
            result += "%4d%9d\n" % (i, score)
            i += 1
        return result
