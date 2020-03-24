#! python3

import random

#gets average of grades
##def average(grade1, grade2, grade3):
##    average = (grade1+grade2+grade3)/3
##    average = round(average, 2)
##    return average

#creates grades array and fills it with random grades from 60 to 100 inclusive
grades = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(grades)):
    for j in range(len(grades[i])-1):
        grades[i][j]=(random.randint(60,100))

#stores the average of the grades
for i in range(len(grades)):
    grades[i][3] = (grades[i][0]+grades[i][1]+grades[i][2])/3
    grades[i][3] = round(grades[i][3], 2)

#declares dict of dict of list with names, grades, and grade averages
grades_per_person = {
    'Keech, Daisy': {grades[0][3]: [grades[0][0], grades[0][1], grades[0][2]]},
    'Hudson, Chase': {grades[1][3]: [grades[1][0], grades[1][1], grades[1][2]]},
    'D\'Amelio, Charli':{grades[2][3]: [grades[2][0], grades[2][1], grades[2][2]]},
    'Warren, Alex':{grades[3][3]: [grades[3][0], grades[3][1], grades[3][2]]}}

#prints the dict in the correct format
for i in grades_per_person:
    print(i+' exam scores:\t', end=' ')
    for j in grades_per_person[i]:
        for k in grades_per_person[i][j]:
            print(k, end=' ')
        print()
        print('Average: '+str(j)+'\n')

input()
