#! /bin/sh
clear

#Takes a number and multiplys it and adds it to itself
function MultAndAdded
{
	read -p "Please enter an integer between 1 and 10 (q to quit): " userNum
	echo " "
	#checks to insure the user number is valid
	if [ $userNum -gt 0 -a $userNum -lt 11 ] > /dev/null 2>&1 ;then
		result=$(((userNum*userNum)+userNum))
	elif [ $userNum == 'q' -o $userNum == 'Q' ] > /dev/null 2>&1 ;then
		toQuit='q'
	else
		#assigns it to zero so the function call will happen again
		result=0
		echo "That is not an integer between 1 and 10. Try again."
		echo " "
	fi
}

#infinate loop
while true;
do
	#reseting vaiables each loop
	result=1
	toQuit='a'

	#calls the function
	MultAndAdded

	#makes sure the user entered a valid input or wants to quit
	if [ $result -eq 0 ] > /dev/null  2>&1 ;then
		continue
	elif [ $toQuit == 'q' ] > /dev/null  2>&1 ;then
		echo "Quiting..."
		break
	else
		echo "The result is $result "
		echo " "
	fi
done
