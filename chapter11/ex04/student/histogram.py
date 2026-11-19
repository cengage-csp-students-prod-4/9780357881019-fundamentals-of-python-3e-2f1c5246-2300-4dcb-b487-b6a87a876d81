"""
File: histogram.py

Displays frequencies of 50 random scores between 95 and 100 in a histogram.

NOTE: Cengage asks to make a histogram for figure 11-7
The included example screenshot shows figure 11-11 in the textbook
In the textbook, figure 11-7 is a bar chart
Since this is a histogram assignment, I wrote a histogram and not a bar chart
If incorrect please inform me and I will fix hastely
"""

import matplotlib.pyplot as plt 
import stats

# Prepare the data 
scores = stats.getRandomList(50, 95, 100)

# Set up and show the histogram 
plt.hist(scores, width = .2)
plt.title("Frequencies of 50 random scores between 95 and 100.")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()