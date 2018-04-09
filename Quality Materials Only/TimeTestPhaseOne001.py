'''
thinking about trying to understand code efficiency by writing specific tests to time iterations of a task to see
subtle differences in approaches to code. Here is a template from which I can expand.
This version iterates in the x axis first then y (like how readers read on a page of text)
the test runs ten times and then takes a time average.'''
import timeit  # imports module for doing precise timing on small bits of code

row0 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]  # The next several  lines of code are just lists over which to iterate
row1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
row2 = [2, 5, 4, 8, 6, 9, 4, 6, 4, 5]
row3 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
row4 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
row5 = [4, 5, 4, 5, 4, 5, 4, 5, 4, 5]
row6 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
row7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
row8 = [2, 3, 2, 4, 2, 5, 1, 3, 4, 5]
row9 = [6, 7, 6, 7, 6, 7, 4, 8, 6, 5]
rows = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9]  # creates a two dimensional array
timercapture = []  # creates an empty list to store my time results
for h in range(1, 10):  # this is a loop made to run my tests 10 times so I may average the results for a better picture
    for i in range(1, 100):  # this loop just adds more steps to "spread out the data"
        for j in range(0, len(rows)):  # begins the vertical part of iteration through the 2D array
            for k in range(0, len(rows[j])):  # begins the horizontal part of iteration through the 2D array
                print (rows[j][k])  # prints out results
    x = timeit.timeit()  # assigns variable to amount of time passed
    timercapture.append(x)  # adds time results to list
avg = sum(timercapture) / float(len(timercapture))  # adds and averages all 10 tests
print ("10 runtimes: " + str(timercapture))
print ("")
print ("Average runtime: " + str(avg))
