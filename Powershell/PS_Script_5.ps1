clear

#list with global flag to let it be modified
$global:name_list = @('Constance Castillo', 'Kerry Goodwin',
 'Dorothy Carson', 'Craig Williams', 'Daryl Guzman', 'Sherman Stewart',
 'Marvin Collier', 'Javier Wilkerson', 'Lena Olson', 'Claudia George',
 'Erik Elliott', 'Traci Peters', 'Jack Burke', 'Jody Turner',
 'Kristy Jenkins', 'Melissa Griffin', 'Shelia Ballard', 'Armando Weaver',
 'Elsie Fitzgerald', 'Ben Evans', 'Lucy Baker', 'Kerry Anderson',
 'Kendra Tran', 'Arnold Wells', 'Anita Aguilar', 'Earnest Reeves',
 'Irving Stone', 'Alice Moore', 'Leigh Parsons', 'Mandy Perez',
 'Rolando Paul', 'Delores Pierce', 'Zachary Webster', 'Eddie Ward',
 'Alvin Soto', 'Ross Welch', 'Tanya Padilla', 'Rachel Logan',
 'Angelica Richards', 'Shelley Lucas', 'Alison Porter', 'Lionel Buchanan',
 'Luis Norman', 'Milton Robinson', 'Ervin Bryant', 'Tabitha Reid',
 'Randal Graves', 'Calvin Murphy', 'Blanca Bell', 'Dean Walters',
 'Elias Klein', 'Madeline White', 'Marty Lewis', 'Beatrice Santiago',
 'Willis Tucker', 'Diane Lloyd', 'Al Harrison', 'Barbara Lawson',
 'Jamie Page', 'Conrad Reynolds', 'Darnell Goodman', 'Derrick Mckenzie',
 'Erika Miller', 'Tasha Todd', 'Aaron Nunez', 'Julio Gomez',
 'Tommie Hunter', 'Darlene Russell', 'Monica Abbott', 'Cassandra Vargas',
 'Gail Obrien', 'Doug Morales', 'Ian James', 'Jean Moran',
 'Carla Ross', 'Marjorie Hanson', 'Clark Sullivan', 'Rick Torres',
 'Byron Hardy', 'Ken Chandler', 'Brendan Carr', 'Richard Francis',
 'Tyler Mitchell', 'Edwin Stevens', 'Paul Santos', 'Jesus Griffith',
 'Maggie Maldonado', 'Isaac Allen', 'Vanessa Thompson', 'Jeremy Barton',
 'Joey Butler', 'Randy Holmes', 'Loretta Pittman', 'Essie Johnston',
 'Felix Weber', 'Gary Hawkins', 'Vivian Bowers', 'Dennis Jefferson',
 'Dale Arnold', 'Joseph Christensen', 'Billie Norton', 'Darla Pope',
 'Tommie Dixon', 'Toby Beck', 'Jodi Payne', 'Marjorie Lowe',
 'Fernando Ballard', 'Jesse Maldonado', 'Elsa Burke', 'Jeanne Vargas',
 'Alton Francis', 'Donald Mitchell', 'Dianna Perry', 'Kristi Stephens',
 'Virgil Goodwin', 'Edmund Newton', 'Luther Huff', 'Hannah Anderson',
 'Emmett Gill', 'Clayton Wallace', 'Tracy Mendez', 'Connie Reeves',
 'Jeanette Hansen', 'Carole Fox', 'Carmen Fowler', 'Alex Diaz',
 'Rick Waters', 'Willis Warren', 'Krista Ferguson', 'Debra Russell',
 'Ellis Christensen', 'Freda Johnston', 'Janis Carpenter', 'Rosemary Sherman',
 'Earnest Peters', 'Kelly West', 'Jorge Caldwell', 'Moses Norris',
 'Erica Riley', 'Ray Gordon', 'Abel Poole', 'Cary Boone',
 'Grant Gomez', 'Denise Chapman', 'Vernon Moran', 'Ben Walker',
 'Francis Benson', 'Andrea Sullivan', 'Wayne Rice', 'Jamie Mason',
 'Jane Figueroa', 'Pat Wade', 'Rudy Bates', 'Clyde Harris',
 'Andre Mathis', 'Carlton Oliver', 'Merle Lee', 'Amber Wright',
 'Russell Becker', 'Natalie Wheeler', 'Maryann Miller', 'Lucia Byrd',
 'Jenny Zimmerman', 'Kari Mccarthy', 'Jeannette Cain', 'Ian Walsh',
 'Herman Martin', 'Ginger Farmer', 'Catherine Williamson', 'Lorena Henderson',
 'Molly Watkins', 'Sherman Ford', 'Adam Gross', 'Alfred Padilla',
 'Dwayne Gibson', 'Shawn Hall', 'Anthony Rios', 'Kelly Thomas',
 'Allan Owens', 'Duane Malone', 'Chris George', 'Dana Holt',
 'Muriel Santiago', 'Shelley Osborne', 'Clinton Ross', 'Kelley Parsons',
 'Sophia Lewis', 'Sylvia Cooper', 'Regina Aguilar', 'Sheila Castillo',
 'Sheri Mcdonald', 'Lynn Hodges', 'Patrick Medina', 'Arlene Tate',
 'Minnie Weber', 'Geneva Pena', 'Byron Collier', 'Veronica Higgins',
 'Leo Roy', 'Nelson Lopez')


#gets a string from the user and finds full names whose first names start with it.
function first_name
{
	$user_str = Read-Host -Prompt "`nEnter the first name, or partial start of the first name"
	$user_str = (Get-Culture).TextInfo.ToTitleCase($user_str.ToLower())
	$count = 0
	write-host
	foreach($i in $global:name_list){
		#if it starts with the string, print it
		if($i.StartsWith($user_str))
		{
			write-host $i
			$count++
		}
	}
	#if no names found, tell the user
	if($count -eq 0)
	{
		write-host "No first names were found starting with $user_str`n"
	}
	else
	{
		write-host 
	}
}

#gets a string from the user and finds full names whose last names start with it.
function last_name
{
	$user_str = Read-Host -Prompt "`nEnter the last name, or partial start of the last name"
	$user_str = (Get-Culture).TextInfo.ToTitleCase($user_str.ToLower())
	$count = 0
	write-host
	foreach($i in $global:name_list)
	{
		#split user name into first and last for comparison
		$last_name = @()
		$last_name += $i.split(" ")
		#if it starts with the string, print it
		if($last_name[1].StartsWith($user_str))
		{
			write-host $i
			$count++
		}
	}
	#if no names found, tell the user
	if($count -eq 0)
	{
		write-host "No last names start with $user_str`n"
	}
	else
	{
		write-host
	}
}

#add a new first and last name to the list
function add_name
{	
	#gets the new name
	$first = Read-Host -Prompt "`nEnter a new first name"
	$last = Read-Host -Prompt "Enter a new last name"
	$first = (Get-Culture).TextInfo.ToTitleCase($first.ToLower())
	$last = (Get-Culture).TextInfo.ToTitleCase($last.ToLower())
	#combines the names and adds it to the list
	$full = $first + " " + $last
	$global:name_list += $full
	write-host "`n$full has been added`n"

}

#deletes a name from the list
function delete_name
{
	write-host "`nThe full name is required. Use menu option one to view full names if needed"
	$temp = @()
	$count = 0
	while(1)
	{
		$del = Read-Host -Prompt "`nEnter the full name, `"1`" to view names, or `"Q`" to quit"
		#calls first_name
		if($del -eq "1"){
			first_name
		}
		#quits
		elseif($del -eq "q" -or $del -eq "Q")
		{
			write-host
			break
		}
		#deletes the entered name
		else
		{
			$del = (Get-Culture).TextInfo.ToTitleCase($del.ToLower())
			#adds all names to not be deleted to a new list
			foreach($i in $global:name_list)
			{
				if($i -eq $del)
				{
					$count += 1
					continue
				}
				$temp += $i
			}
			#if no name found then let the user know the list did not change
			if($count -eq 0)
			{
				write-host "`n$del does not exist. Please try again.`n"
				continue
			}
			#assigns gloabl list to temp list
			$global:name_list = $temp
			write-host "`n$del has been deleted`n"
			break
		}
	}
}

while(1)
{
	#asks for user choice then calls the correct function
	write-host "Please select from the following options:`n`n`t1.   List all names starting with one or more letters of the first name"
	write-host "`t2.   List all names starting with one or more letters of the last name`n`t3.   Add a name`n`t4.   Delete a name`n`t5.   Exit"
	$user_choice = Read-Host -Prompt "`nOption #"
	if($user_choice -eq "1")
	{
		first_name
	}
	elseif($user_choice -eq "2")
	{
		last_name
	}
	elseif($user_choice -eq "3")
	{
		add_name
	}
	elseif($user_choice -eq "4")
	{
		delete_name
	}
	elseif($user_choice -eq "5")
	{
		break
	}
	else
	{
		write-host "Not a valid option, please try again.`n"
	}
}







