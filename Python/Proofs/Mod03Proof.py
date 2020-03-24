#! python3

#Jacob Hinchey

#given lists
list_one = [100,'Potential',-76,'opposed','storage','Drum',78,-17,75,'Organize','dome','reign',480,'claim',148,'hope',105,'claim',100,'second']
list_two = ['Palace',94,'leadership','Second','Layout',-118,-295,-60,'tiptoe','Denial',-231,'Organize',-240,'Countryside','reign','Responsibility','Burial','Drown',133,180]
list_three = ['censorship',181,'corner',148,'Epicalyx',-159,'Opposed',97,'sigh',104,'Claim',97,'Taste',-60,'Difficulty',288,'profession',467,'ensure',223]
list_of_lists = [[395,-498,'Hope'],[-10,'undertake',-448],[-345,238,'dictionary'],['decline',223,-139],['Countryside',482,235],[97,'imperial',]]

#lists to hold answers
task1 = []
task2_even = []
task2_odd = []
task3 = []
task4 = []

#Task1-append each element in or of index from list one and two
for i in range(len(list_one)):
    task1.append(list_one[i])
    task1.append(list_two[i])

print('\nTASK 1')
print(task1)

#Task2-add even indexs to one list and odd to another
for i in range(0, len(list_three), 2):
    task2_even.append(list_three[i])
    task2_odd.append(list_three[i+1])

print('\nTASK 2')
print(task2_even)
print()
print(task2_odd)
print()

#Task3-Add all ints in list one to a list
for i in list_one:
    try:
        to_add = int(i)
        task3.append(to_add)
    except:
        continue

print('\nTASK 3')
print(task3)

#Task4-turn a list of lists into a normal list
for i in list_of_lists:
    for j in range(len(i)):
        task4.append(i[j])

print('\nTASK 4')
print(task4)

