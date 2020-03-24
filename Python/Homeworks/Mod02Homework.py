#! python3

import sys

#Takes input and squares it then adds the same origainal number to it
def square_add(user_input): 
    return (user_input ** user_input) + user_input

#Loop that runs forever
while True:
    #Gets user input
    user_input = input('\nPlease enter an integer between 1 and 10: ')
    
    #Checks to make sure the user input is a int
    try:
        int(user_input)
    except:
        print('That is not an integer. Please try again.')
        continue
    
    #Checks to make sure user input is between 1 and 10 non inclusive
    if(1 < int(user_input) < 10):
        #prints result of putting user_input into square_add
        print(square_add(int(user_input)))
        #Asks user if they want to quit then imediatly close the prompt
        wantOut = input('\nPress Q to exit, anything else to go again: ')
        
        #If the user typed Q, then exit
        if(wantOut == 'Q'):
            sys.exit()
            
    #Prints instructions again if not in range       
    else:
        print('Integer out of bounds. Please try again.')
        continue

