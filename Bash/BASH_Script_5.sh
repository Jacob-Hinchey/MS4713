#! /bin/bash

name_array=('Constance_Castillo' 'Kerry_Goodwin' 'Dorothy_Carson' 'Craig_Williams' 
'Daryl_Guzman' 'Sherman_Stewart' 'Marvin_Collier' 'Javier_Wilkerson' 'Lena_Olson' 
'Claudia_George' 'Erik_Elliott' 'Traci_Peters' 'Jack_Burke' 'Jody_Turner' 'Kristy_Jenkins' 
'Melissa_Griffin' 'Shelia_Ballard' 'Armando_Weaver' 'Elsie_Fitzgerald' 'Ben_Evans' 'Lucy_Baker' 
'Kerry_Anderson' 'Kendra_Tran' 'Arnold_Wells' 'Anita_Aguilar' 'Earnest_Reeves' 'Irving_Stone' 
'Alice_Moore' 'Leigh_Parsons' 'Mandy_Perez' 'Rolando_Paul' 'Delores_Pierce' 'Zachary_Webster' 
'Eddie_Ward' 'Alvin_Soto' 'Ross_Welch' 'Tanya_Padilla' 'Rachel_Logan' 'Angelica_Richards' 
'Shelley_Lucas' 'Alison_Porter' 'Lionel_Buchanan' 'Luis_Norman' 'Milton_Robinson' 'Ervin_Bryant' 
'Tabitha_Reid' 'Randal_Graves' 'Calvin_Murphy' 'Blanca_Bell' 'Dean_Walters' 'Elias_Klein' 
'Madeline_White' 'Marty_Lewis' 'Beatrice_Santiago' 'Willis_Tucker' 'Diane_Lloyd' 'Al_Harrison' 
'Barbara_Lawson' 'Jamie_Page' 'Conrad_Reynolds' 'Darnell_Goodman' 'Derrick_Mckenzie' 
'Erika_Miller' 'Tasha_Todd' 'Aaron_Nunez' 'Julio_Gomez' 'Tommie_Hunter' 'Darlene_Russell' 
'Monica_Abbott' 'Cassandra_Vargas' 'Gail_Obrien' 'Doug_Morales' 'Ian_James' 'Jean_Moran' 
'Carla_Ross' 'Marjorie_Hanson' 'Clark_Sullivan' 'Rick_Torres' 'Byron_Hardy' 'Ken_Chandler' 
'Brendan_Carr' 'Richard_Francis' 'Tyler_Mitchell' 'Edwin_Stevens' 'Paul_Santos' 
'Jesus_Griffith' 'Maggie_Maldonado' 'Isaac_Allen' 'Vanessa_Thompson' 'Jeremy_Barton' 
'Joey_Butler' 'Randy_Holmes' 'Loretta_Pittman' 'Essie_Johnston' 'Felix_Weber' 'Gary_Hawkins' 
'Vivian_Bowers' 'Dennis_Jefferson' 'Dale_Arnold' 'Joseph_Christensen' 'Billie_Norton' 
'Darla_Pope' 'Tommie_Dixon' 'Toby_Beck' 'Jodi_Payne' 'Marjorie_Lowe' 'Fernando_Ballard' 
'Jesse_Maldonado' 'Elsa_Burke' 'Jeanne_Vargas' 'Alton_Francis' 'Donald_Mitchell' 'Dianna_Perry' 
'Kristi_Stephens' 'Virgil_Goodwin' 'Edmund_Newton' 'Luther_Huff' 'Hannah_Anderson' 'Emmett_Gill' 
'Clayton_Wallace' 'Tracy_Mendez' 'Connie_Reeves' 'Jeanette_Hansen' 'Carole_Fox' 'Carmen_Fowler' 
'Alex_Diaz' 'Rick_Waters' 'Willis_Warren' 'Krista_Ferguson' 'Debra_Russell' 'Ellis_Christensen' 
'Freda_Johnston' 'Janis_Carpenter' 'Rosemary_Sherman' 'Earnest_Peters' 'Kelly_West' 
'Jorge_Caldwell' 'Moses_Norris' 'Erica_Riley' 'Ray_Gordon' 'Abel_Poole' 'Cary_Boone' 
'Grant_Gomez' 'Denise_Chapman' 'Vernon_Moran' 'Ben_Walker' 'Francis_Benson' 'Andrea_Sullivan' 
'Wayne_Rice' 'Jamie_Mason' 'Jane_Figueroa' 'Pat_Wade' 'Rudy_Bates' 'Clyde_Harris' 'Andre_Mathis' 
'Carlton_Oliver' 'Merle_Lee' 'Amber_Wright' 'Russell_Becker' 'Natalie_Wheeler' 'Maryann_Miller' 
'Lucia_Byrd' 'Jenny_Zimmerman' 'Kari_Mccarthy' 'Jeannette_Cain' 'Ian_Walsh' 'Herman_Martin' 
'Ginger_Farmer' 'Catherine_Williamson' 'Lorena_Henderson' 'Molly_Watkins' 'Sherman_Ford' 
'Adam_Gross' 'Alfred_Padilla' 'Dwayne_Gibson' 'Shawn_Hall' 'Anthony_Rios' 'Kelly_Thomas' 
'Allan_Owens' 'Duane_Malone' 'Chris_George' 'Dana_Holt' 'Muriel_Santiago' 'Shelley_Osborne' 
'Clinton_Ross' 'Kelley_Parsons' 'Sophia_Lewis' 'Sylvia_Cooper' 'Regina_Aguilar' 
'Sheila_Castillo' 'Sheri_Mcdonald' 'Lynn_Hodges' 'Patrick_Medina' 'Arlene_Tate' 'Minnie_Weber' 
'Geneva_Pena' 'Byron_Collier' 'Veronica_Higgins' 'Leo_Roy' 'Nelson_Lopez')

#finds people based on partial first names
function first_name
{
	count=0
	echo " "
	read -p "Enter the first name, or a partial start of the first name: " first_n
	echo " "
	#sets input to lower for comparison, and checks it against all of the 
	#names in the array to see if it matches
	first_n=$(echo $first_n | tr [:upper:] [:lower:])
	for i in ${name_array[*]};
	do
		temp=$(echo $i | tr [:upper:] [:lower:])
		if [[ $temp = "$first_n"* ]];then
			temp=$(echo $i | tr "_" " ")
			echo $temp
			count=$(($count+1))
		fi
	done
	#if no matches are found
	if [ $count -eq 0 ];then
	
		
		fir=$(echo ${first_n:0:1} | tr [:lower:] [:upper:])
		last=${first_n:1}
		to_print="$fir$last"

		echo "No first name was found starting with $to_print"
	fi
}

#prints names based on partial last name
function last_name
{
	echo " "
	read -p "Enter the last name, or a partial start of the last name: " last_n
	echo " "
	#sets to lower case and adds an underscore for comparison
	holder=$last_n
	last_n=$(echo $last_n | tr [:upper:] [:lower:])
	last_n="_${last_n}"
	count=0
	#checks each index for matches
	for i in ${name_array[*]};
	do
		temp=$(echo $i | tr [:upper:] [:lower:])
		if [[ $temp = *"$last_n"* ]];then
			temp=$(echo $i | tr "_" " ")
			echo $temp
			count=$(($count+1))
		fi
	
	done
	#if not matches were found
	if [ $count -eq 0 ];then
		fir=$(echo ${holder:0:1} | tr [:lower:] [:upper:])
		last=${holder:1}
		holder="$fir$last"
		echo "No last names begin with $holder"
	fi
	
}

#adds a name to the list
function add_name
{
	full_n=" "
	to_print=" "
	echo " "
	#to insure the person uses the function correctly
	while true;
	do
		read -p "Enter the new first name: " first_n
		#if they entered first and last name, start over
		if [[ $first_n = *" "* ]];then
			echo "Just the first name, please. No Spaces."
			continue
		fi
		read -p "Enter the new last name: " last_n
		echo " "
		#sets to title case and combines the names
		first_n=$(echo $first_n | tr [:upper:] [:lower:])
		last_n=$(echo $last_n | tr [:upper:] [:lower:])

		first_f=$(echo ${first_n:0:1} | tr [:lower:] [:upper:])
		remain_f=${first_n:1}
		first_n="$first_f$remain_f"
		
		first_l=$(echo ${last_n:0:1} | tr [:lower:] [:upper:])
		remain_l=${last_n:1}
		last_n="$first_l$remain_l"
	
		full_n="${first_n}_${last_n}"
		to_print="${first_n} ${last_n}"
		break		
	done	
	#adds the person to the array
	name_array+=($full_n)	
	echo "$to_print has been added"
}
#removes a person from the array
function delete_name
{
	while true;
	do	
		echo " "
		echo "Delete a name by entering the full name ie: John Smith"
		read -p "Enter the full name (0 to return to the main menu. 1 to search first names): " user_input
		#allows user to quit or user first_name to find person to delete
		if [ $user_input == "q" ] || [ $user_input == "Q" ] > /dev/null 2>&1 ;then
			break
		elif [ $user_input -eq 1 ] > /dev/null 2>&1 ;then
			first_name
			continue
		else
			#put the name into title case
			user_input=$(echo $user_input | tr [:upper:] [:lower:])
			first_n=$(echo $user_input | cut -d " " -f 1)
			last_n=$(echo $user_input | cut -d " " -f2)

			first_f=$(echo ${first_n:0:1} | tr [:lower:] [:upper:])
			remain_f=${first_n:1}
			first_n="$first_f$remain_f"
	
			first_l=$(echo ${last_n:0:1} | tr [:lower:] [:upper:])
			remain_l=${last_n:1}
			last_n="$first_l$remain_l"

			full_n="${first_n}_${last_n}"
			full_n_space="${first_n} ${last_n}" 
			count=0
			declare -a new_names=()
			#go through array and add to new array if it is not the name to be
			#deleted
			for i in ${name_array[*]};
			do
				if [ $full_n == $i ];then
					count=$(($count+1))
					continue
				else
					new_names+=($i)
				fi	
			done
			#if name is not in the list
			if [ $count -eq 0 ];then
				echo "$full_n_space was not found in the array"
				continue
			fi
			#set name_array to new array to delete the name
			name_array=("${new_names[*]}")
			echo " "
			echo "$full_n_space has been deleted from the array"
		fi
	done
}



#menu
while true;
do
	echo " "
	echo "Please select from the following options:"
	echo " "
	echo "	1.  List all names starting with one or more letters of the first name"
	echo "	2.  List all names starting with one or more letters of the last name"
	echo "	3.  Add a name"
	echo "	4.  Delete a name"
	echo "	5.  Quit"
	echo " "
	read -p "Option #:" user_choice
	#takes user to function based on input
	if [ $user_choice -eq 1 ] > /dev/null 2>&1 ;then
		first_name
	elif [ $user_choice -eq 2 ] > /dev/null 2>&1 ;then
		last_name
	elif [ $user_choice -eq 3 ] > /dev/null 2>&1 ;then
		add_name
	elif [ $user_choice -eq 4 ] > /dev/null 2>&1 ;then
		delete_name
	elif [ $user_choice -eq 5 ] > /dev/null 2>&1 ;then
		break
	else
		echo "Not a valid option. Please try again."
	fi
done