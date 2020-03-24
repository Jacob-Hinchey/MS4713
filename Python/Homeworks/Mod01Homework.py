#! python3
import random

START_PRICE = 100 #const base val
paid_amount = 0 #variable declaration for later

#offset the base amount by -15,-10, -5, 0, 5, 10, or 15
variation = random.randint(-3, 3)
variation *= 5
price = START_PRICE + variation

#start user interation, store type of drink they want, and tell them the price
print('Welcome to the soda machine. You can enter values of 5, 10, or 25 in payment')
drink_type = input('What type of soda would you like? ')
print('The current price of ' + drink_type + ' is ' + str(price) + ' cents')

#infinate loop until total is paid
while True:
    
    #takes in coin value and subtacts total paid value from the price
    print('Enter a coin: ')
    inserted_coin = input()
    paid_amount += int(inserted_coin)
    remaining = price - paid_amount
    
    #if remaining amount is less than zero then tell them how much they owe
    if remaining > 0:
        print('You still owe ' + str(remaining))

    #if overpaid then refund and exit the loop
    elif remaining < 0:
        print('You have been refunded ' + str(abs(remaining)) + ' cents')
        break

    #if paid amount equals the price then do nothing and exit the loop
    else:
        break
print('Enjoy your ' + drink_type + '!')
