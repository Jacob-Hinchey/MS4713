#! python3

import random

source_string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 abcdefghijklmnopqrstuvwxyz @%+\/'!#$^?:,(){}[]~`-_. "

#function that takes an int and makes a random password from the source string
def passward_generator(characters):
    generated = ''
    for i in range(characters):
        generated += source_string[random.randint(0, len(source_string)-1)]
    return generated


#will run until password is generated
while True:

    #total numbers of fails for each possibility
    whitespace_fail = 0
    two_cap = 0
    two_num = 0
    two_special = 0
    no_cap = 0
    no_num = 0
    no_special = 0
    total_fail = 0

    #get the password length
    characters = input('Enter a password length from 12 to 20: ')
    try:
        characters = int(characters)
    except:
        print('That is not a number, try again')
        continue

    #if in is not between 12 and 20 ask the user again
    if characters < 12 or characters > 20:
        print('Must be between 12 and 20')
        continue

    #run until password is successful
    while True:

        #call password generator
        password = passward_generator(characters)

        #variables to hold is a failure was detected and what kind
        whitespace = 0
        cap = 0
        special = 0
        num = 0
        double_cap = 0
        double_special = 0
        double_num = 0

        #check to make sure there are no white spaces and enough of each type of character
        for i in password:
            if i in source_string[1:27]:
                cap += 1
            elif i in source_string[27:37]:
                num += 1
            elif i.isspace():
                whitespace += 1
            elif i in source_string[65:89]:
                special += 1

        #checks to make sure no two letters are together that are now allowed
        for i in range(len(password)-1):
            if password[i] in source_string[1:27] and password[i + 1] in source_string[1:27]:
                double_cap += 1
            elif password[i] in source_string[27:37] and password[i + 1] in source_string[27:37]:
                double_num += 1
            elif password[i] in source_string[65:89] and password[i + 1] in source_string[65:89]:
                double_special += 1

        #if an error was detected, add it to the total for that type of error
        if whitespace >= 1:
            whitespace_fail += 1
        if cap < 2:
            no_cap += 1
        if special < 2:
            no_special += 1
        if num < 2:
            no_num += 1
        if double_cap >= 1:
            two_cap += 1
        if double_special >= 1:
            two_special += 1
        if double_num >= 1:
            two_num += 1

        #THIS WILL COUNT HOW MANY TIMES A NEW PASSWORD HAD TO BE GENERATED AND REPORT THAT AS A FAILURE
        #THIS WILL NOT COUNT HOW MANY FAILURES THERE MAY BE IN ONE PASSWORD, TO DO THAT SIMPLY ADD A
        #BREAK AND TOTAL FAILURE COUNTER AFTER EACH FOUND FAILURE.
        if whitespace >= 1 or cap < 2 or special < 2 or num < 2 or double_cap >= 1 \
           or double_special >= 1 or double_num >= 1:
            total_fail += 1
        else:
            break
    break

#prints the results
print('\nGood password generated! \n\n\t' + password)
input('\nFailure Causes:\n\n\tSpaces in password: ' + str(whitespace_fail) \
              + '\n\tTwo capital letters next to each other: ' + str(two_cap) \
              + '\n\tTwo numbers next to each other: ' + str(two_num) \
              + '\n\tTwo special characters next to each other: ' + str(two_special) \
              + '\n\tLess than two capital letters: ' + str(no_cap) \
              + '\n\tLess than two numbers: ' + str(no_num) \
              + '\n\tLess than two special characters: ' + str(no_special) \
              + '\n\nTotal number of Failures: ' + str(total_fail))
