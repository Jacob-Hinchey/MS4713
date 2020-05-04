#! /bin/sh

declare -a arr=()

#inserts a marvel char at a random index
function MarvelInsert
{
	newRand=$((RANDOM%10))
	declare -a newArr=()
	count=0

	#get the array before the random
	while [ $count -lt $newRand ];
	do
		newArr+=(${arr[$count]})
		count=$(($count+1))
	done
	#insert marvel char and add the rest of the list
	newArr+=($1)
	count=$newRand
	while [ $count -lt 10 ];
	do
		newArr+=(${arr[$count]})
		count=$(($count+1))
	done
	echo " "
	echo "$1 is at the position $newRand in the array"
	echo " "
	echo "The array is now: ${newArr[*]}"
	echo " "


}

echo " "
echo "Create an array filled with 10 items"
echo "Be sure to get a mix of floating point numbers, integers, and  text"
echo " "
#fill the array and the spaces with _
count=0
while [ $count -lt 10 ];
do
	read -p "Please enter a number or word for index position $count: " toAdd
	arr+=($( echo $toAdd | tr " " "_"))
	count=$(($count+1))
done

echo " "

#Check to make sure it has 10 items
if [ ${#arr[*]} -eq 10 ] ;then
	echo "This array has 10 items"
else
	echo "This array does not have 10 items"
fi

#print the array
echo " "
echo "This is the array:"
echo ${arr[*]}
echo " "

#switch the first and last element and print it
temp=${arr[9]}
arr[9]=${arr[0]}
arr[0]=$temp

echo "This is the array after swapping the first and last items:"
echo ${arr[*]}
echo " "

#print the first and last three elements
echo "These are the first three and last three items in the array:"
echo "${arr[*]:0:3} ${arr[*]:7:3}"
echo " "

#print on new lines and see if it has cat
flag=0
for i in ${arr[*]};
	do
		echo $i
		if [ $i == "cat" ] ;then
			flag=1
		fi
	done

echo " "
if [ $flag -eq 1 ] ;then
	echo "There is a cat in my array"
else
	echo "There is not a cat in my array"
fi
echo " "

#get marvel char name and call the function to insert it
read -p "Please enter the name of a Marvel character: " marvelChar
marvelChar=$( echo $marvelChar | tr " " "_")
MarvelInsert $marvelChar

#get an array of ints, sort it and print it
declare -a intArr=()
for i in ${arr[*]};
do
	if [[ $i =~ ^-?[0-9]+$ ]] ;then
		intArr+=($i)
	fi
done

intArr=($(for i in ${intArr[*]}; do echo $i; done | sort -n ))
echo "The integers in the original array, sorted, are: ${intArr[*]}"
echo " "
read -p "Press enter to end the script: "
		
