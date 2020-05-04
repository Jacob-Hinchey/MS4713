$counter = 0
$arr = @()

#function to get marvel character and insert it into array
function MarvelCharacter($arr){
	#gets marvel character and random number
	$marvel = Read-Host -Prompt "Please insert the name of a Marvel character"
	$myRan = Get-Random -Minimum 0 -Maximum 10
	#new array with marvel character in it gets values less thah the random
	$newArr = @()
	for($i=0;$i -lt 10; $i++)
	{
		if($i -lt $myRan)
		{
			$newArr += $arr[$i]
		}
	}


	#leave space for character then add the rest of the list
	$newArr += 0
	for($i=$myRan;$i -lt 11;$i++)
	{
		$newArr += $arr[$i]
	}

	#add the character in the saved space then print index and new array
	$newArr[$myRan] = $marvel
	write-host "`n$marvel is at position $myRan in the array"
	write-host "$newArr"
}

write-host "Create an array filled with some words and numbers"

#takes items into array from user
while($counter -lt 10)
{
	$item = Read-Host -Prompt "Please enter a number or word"
	$arr += $item
	$counter= $counter +1
}

#boolean for length ==10
$tenItems = ($arr.Length -eq 10)

write-host "`nThis array has 10 items. $tenitems`n"

#print array
write-host "This is the array:`n$arr"

#switch the first and last value
$temp = $arr[0]
$arr[0] = $arr[9]
$arr[9] = $temp

write-host "`nThis is the array after swapping the first and last items:`n$arr`n"

#print the first three and last three indexes
write-host "These are the first three items and the last three items in the array:"
write-host $arr[0] $arr[1] $arr[2] $arr[7] $arr[8] $arr[9]"`n"
write-host "These are the individual items of the array:"

#print indexes individually
for($i=0; $i -lt 10 ; $i++)
{
	write-host $arr[$i]
}

#check to see if cat is in the array
if($arr.Contains("cat"))
{
	write-host "`nThere is a cat in my array`n"
}
else 
{
	write-host "`nThere is not a cat in my array`n"
}

#calls marvel character
MarvelCharacter($arr)

$intarr = @()
#int array for ordered list later
for($i=0;$i -lt 10;$i++)
{	
	if($arr[$i].Contains(".")){
		continue
	}
	try
	{
		$temp= [int]$arr[$i]
		$intarr += $temp
	}
	catch{
		continue
	}
}


#sort int array then print it out
$intarr =  $intarr|Sort
write-host "`nThe intager in the original array, sorted are: $intarr"

Read-Host -Prompt "`nPress enter to close the program"
