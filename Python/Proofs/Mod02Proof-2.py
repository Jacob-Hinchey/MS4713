#! python3

import random

#function that takes five inputs and places them into a print
def madlib(name, whole_num, item, animal, emotion):
    print('\nOne day ' + name + ' went to the store and bought '\
          + str(int(whole_num) * 1.3) + ' ' + item + '.\n'\
          + name + ' fed these to the ' + animal \
          + ', which made it very ' + emotion + '.\n')
            
    
#forever iterating loop
while True:
    print('\nLet\'s play a quick round of madlibs. I need some info from you.')
    #these are the five variables to hold user data
    name = input('A person\'s name: ')
    whole_num = input('a whole number, like 3 or 15: ')
    #insures the user types a number, assigns them one if not
    try:
        whole_num = int(whole_num)
    except:
        whole_num = random.randint(2, 37)
        print('That\'s not an integer so I\'ll pick for you. I\'ve chosen ' + str(whole_num))

    item = input('Some objects plural, like pencils or cabbages: ')
    animal = input('A type of animal: ')
    emotion = input('An emotion: ')

    #calls madlib function with user input
    madlib(name, whole_num, item, animal, emotion)

    #asks the user if they want to play again
    user_choice = input('Press Y to play again: ')
    if(user_choice == 'y' or user_choice == 'Y'):
        continue
    else:
        break

input()
