#! python3

import random
import copy

card_deck = [['Ace of Spades', 'King of Spades', \
            'Queen of Spades', 'Jack of Spades', \
            '10 of Spades', '9 of Spades', \
            '8 of Spades', '7 of Spades', \
            '6 of Spades', '5 of Spades', \
            '4 of Spades', '3 of Spades', \
            '2 of Spades'], \
            ['Ace of Diamonds', 'King of Diamonds', \
            'Queen of Diamonds', 'Jack of Diamonds', \
            '10 of Diamonds', '9 of Diamonds', \
            '8 of Diamonds', '7 of Diamonds', \
            '6 of Diamonds', '5 of Diamonds', \
            '4 of Diamonds', '3 of Diamonds', \
            '2 of Diamonds'],\
            ['Ace of Clubs', 'King of Clubs', \
            'Queen of Clubs', 'Jack of Clubs', \
            '10 of Clubs', '9 of Clubs', \
            '8 of Clubs', '7 of Clubs', \
            '6 of Clubs', '5 of Clubs', \
            '4 of Clubs', '3 of Clubs', \
            '2 of Clubs'],\
            ['Ace of Hearts', 'King of Hearts', \
            'Queen of Hearts', 'Jack of Hearts', \
            '10 of Hearts', '9 of Hearts', \
            '8 of Hearts', '7 of Hearts', \
            '6 of Hearts', '5 of Hearts', \
            '4 of Hearts', '3 of Hearts', \
            '2 of Hearts']]

#creates the deck for the game
current_deck = copy.deepcopy(card_deck)

#function to print random card from deck when called
def card_deal():
    while True:
        
        #Checks to see if the deck is empty
        if (len(current_deck) == 0):
            print('No cards are in the deck')
            break
        
        #picks a random suit and stores it
        suit_to_pick = random.randint(0, len(current_deck)-1)
        current_suit = current_deck[suit_to_pick]

        #if that suit is empty, delete it and try again
        if (len(current_deck[suit_to_pick]) == 0):
            current_deck.remove(current_suit)
            continue
        
        #picks a random card in the suit and stores it
        card_to_pick = random.randint(0, len(current_deck[suit_to_pick])-1)
        current_card = current_deck[suit_to_pick][card_to_pick]
        
        #prints the card
        print(current_card)
        #removes that card from the deck and exits function
        current_deck[suit_to_pick].remove(current_card)
        break
        
print('The deck has been shuffled!')
while True:
    times = input('How many cards would you like to draw? ')
    
    #tries to convert user input into an int and rejects if not possible
    try:
        number_times = int(times)
    except:
        print('That is not an integer. Try again!')
        continue
    
    #takes the user number and deals cards using card_deal func
    count = 0
    while number_times > count:
        card_deal()
        count += 1
        
    #asks the user if they want to draw again, suffle, or quit
    user_response = input('To reshuffle the deck type r, to exit type q, anything else to pick from the same deck: ')
    if user_response == 'q':
        break
    elif user_response == 'r':
        current_deck = copy.deepcopy(card_deck)
    else:
        continue
input('Thanks for playing! Press enter to exit')





