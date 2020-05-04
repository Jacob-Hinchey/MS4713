#gets user input and multiplies it by itsself then adds the same number to it
function MultAndAdded ()
{
	$ans = Read-Host -Prompt "Please enter an integer between 1 and 10"
	write-host ""

	#checks to make sure it is an int
	$difference=0
	try
	{
		$difference = $ans - [int]$ans
	}
	catch
	{
		write-host "That is not a number. Please try again`n"
		return 0
	}
	if($difference -ne 0)
	{
		write-host "That is not a integer. Please try again`n"
		return 0
	}

	#makes sure it is within 1 to 10 inclusive
	$ans = $ans/1
	if($ans -gt 10)
	{
		write-host "Integer out of bounds. Please try again`n"
		return 0
	}
	if($ans -lt 1)
	{
		write-host "Integer out of bounds. Please try again`n"
		return 0
	}
	#gets result and returns it
	$ans = ($ans*$ans)+$ans
	return $ans
}

#runs until break
while($true)
{
	
	#calls function
	$result = MultAndAdded

	#checks to make sure result is valid, if not start the loop again
	if($result -eq 0)
	{
		continue
	}

	#Prints result
	write-host "$result`n"

	#gets user choice on whether to quit or not
	$cont = Read-Host -Prompt "Press Q to exit, anything else to go again"
	write-host ""

	if($cont.ToUpper() -eq 'Q')
	{
		break
	}

}