clear

Write-Host "Welcome to the Soda Machine. You can enter values of 5, 10, or 25`n"
#Gets user soda wanted
$drink_type = Read-Host -Prompt "What type of soda would you like?"

#gets a random price of 85,90,95,100,105,110, or 115
$start_price = 100
$myRan = Get-Random -Minimum -3 -Maximum 4
$myRan = $myRan * 5

clear

#tells user the price of their drinks
$start_price = $start_price + $myRan
Write-Host "The current price of $drink_type is $start_price cents`n"

#While not break
while ($true)
{
  #Gets user input and checks to see make sure it is 5,10, or 25 if not it tells the user
  $coin = Read-Host -Prompt "Enter a coin"
  clear
  try
  {
    $coin = $coin/1
  }
  catch
  {
    Write-Host "That is not a valid amount.`n"
    Write-Host "You still owe $start_price cents.`n"
    continue
  }
  if($coin -eq 5)
  {
    Write-Host "You have inserted a nickle.`n"
    $start_price = $start_price - 5
  }
  elseif($coin -eq 10)
  {
    Write-Host "You have inserted a dime.`n"
    $start_price = $start_price - 10
  }
  elseif($coin -eq 25)
  {
    Write-Host "You have inserted a quarter.`n"
    $start_price = $start_price - 25
  }
  else
  {
    Write-Host "That is not a valid amount.`n"
  }
  #checks to see if the user has paid enough for the drink and responds appropriately
  if($start_price -gt 0)
  {
    Write-Host "You still owe $start_price cents.`n"
  }
  elseif($start_price -eq 0)
  {
    Write-Host "Enjoy your $drink_type!`n"
    break
  }
  elseif($start_price -lt 0)
  {
    $start_price = $start_price * -1
    Write-Host "You have been refunded $start_price. cents`n"
    Write-Host "Enjoy your $drink_type!`n"
    break
  }
}
Read-Host -Prompt "Press enter to close the program"
