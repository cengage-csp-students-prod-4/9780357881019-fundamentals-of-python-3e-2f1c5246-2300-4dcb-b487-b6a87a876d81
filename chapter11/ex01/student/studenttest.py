from student import Student

jeff = Student("Jeff", 10)
jeff.randomizeScores(10, 50, 100)
mean = jeff.getMean()
median = jeff.getMedian()
mode = jeff.getMode()
std = jeff.getStd()

print(jeff,
      "\nMean: ", mean,
      "\nMedian: ", median,
      "\nMode: ", mode,
      "\nStandard deviation: ", std,
      sep = ""
)