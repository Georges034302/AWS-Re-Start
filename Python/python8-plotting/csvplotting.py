from numpy import random
import matplotlib.pyplot as plt
import csv
import collections
import numpy as np

grades = [] # will be used to collect the grades from csv

with open('students.csv','r') as handler:
    rows = csv.reader(handler,delimiter=',')
    next(rows) # this will skip the first row - the header
    for row in rows:
        grades.append(row[3]) # storing the grade from each row
        
counter = collections.Counter(grades) # determine the frequency of each grade
frequency = counter.values() # create a list of frequencies

gradeset = np.unique(np.array(grades)) # This will collect the unique grades for the labels

plt.pie(frequency,labels=gradeset,autopct='%.2f%%')
plt.title('Grades Distribution',fontsize=20)
plt.legend(title='Grades:')
plt.show()