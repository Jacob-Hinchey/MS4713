#! python3

import sys
import random

print('You will play the number guessing game three times. Each time you will have five chances to guess the number that is between 1 and 10 (inclusive)\n')

count = 1

#happens three times
while (count < 4):
    
    #asks usre for input and creates randomint
    print('This is game number ' + str(count) + '\n')
    num_rand = random.randint(1,10)
    #print(str(num_rand))
    
    #gives user three chances
    for i in range(0,5,1):
        user_guess = input('This is chance ' + str(i+1) + '\nEnter an integer between 1 and 10: ')

        #checks to see if equal
        if (int(user_guess) == num_rand):
            print('\n\nYou Win!\n\n\n')
            break
        #tell if lost
        elif (i == 4):
            print('\n\nYou are out of chances. You lose\n\n')
        #tell incorrect
        else:
            print('Incorrect. Try again.\n')
    count += 1
input('Press enter to close the game:')
        
        
        
    
