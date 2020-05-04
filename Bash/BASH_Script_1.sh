#! /bin/sh
clear

#for base price
BASE_PRICE=100
echo "Welcome to the soda machine. You can enter values of 5, 10, or 25 in payment."
echo " "

#get the type of soda the user wants
read -p "What type of soda would you like? " soda_type

#set cost to 85,90,95,100,105,110,115 randomly
variant=$((( $RANDOM%7)-3))
variant=$(($variant*5))
echo " "
variant=$(($variant+$BASE_PRICE))
echo "The current price of $soda_type is $variant cents"

#will run until soda is paid
while true;
do
	echo " "
	#get the coin the user wants to enter
	read -p "Enter a coin: " user_input
	
	#check to see if in is a dime,nickle,or quarter if not tell them
	if [ $user_input -eq 25 ] > /dev/null 2>&1 ;then
		echo "You have inserted a quarter"
		variant=$(($variant-$user_input))
	elif [ $user_input -eq 10 ] > /dev/null 2>&1 ;then
		echo "You have inserted a dime"
		variant=$(($variant-$user_input))
	elif [ $user_input -eq 5 ] > /dev/null 2>&1 ;then
		echo "You have inserted a nickle"
		variant=$(($variant-$user_input))
	else
		echo "That is not a valid amount"
	fi	
	
	#check to see if they paid off the amount
	if [ $variant -gt 0 ] ;then
		echo "You still owe $variant cents"
	elif [ $variant -eq 0 ] ;then
		echo " "
		echo "Your $soda_type is being dispensed. Thank you!"
		break
	else 
		echo " "
		variant=$(($variant*-1))
		echo "You have been refunded $variant cents."
		echo " "
		echo "Your $soda_type is being dispensed. Thank you!"
		break
	fi

done
echo " "
read -p "Press the enter key to close the script"