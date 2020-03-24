#! python3

name_list = ['Constance Castillo', 'Kerry Goodwin',
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
 'Leo Roy', 'Nelson Lopez']

#Finds names based on first letter given for first names
def first_name():

    #asks the user what the first letter of the first name is and prints it
    first_letter = input('What letter does the first name begin with? ')
    counter = 0
    print()
    for i in name_list:
        if i.startswith(first_letter.upper()):
            print(i)
            counter += 1

    #if no names are found, tell the user
    if counter == 0:
        print('No first names were found starting with the letter ' + first_letter.upper())
    print()
    
#Finds names based on first letter given for last names
def last_name():
    
    #splits names into arrays of first and last names
    names = []
    for i in range(len(name_list)):
        names.append(name_list[i].split(' '))

    #puts the first name into a list and the last name into another
    first_names=[]
    last_names=[]
    for i in range(len(name_list)):
        first_names.append(names[i][0])
        last_names.append(names[i][1])

    #Combines first and last names in a 'last, first' format in a new list
    backwards_names =[]
    for i in range(len(name_list)):
        to_add = last_names[i] + ', ' + first_names[i]
        backwards_names.append(to_add)

    #asks the user what the first letter of the last name is and prints it
    first_letter = input('What letter does the last name begin with? ')
    counter = 0
    print()
    for i in backwards_names:
        if i.startswith(first_letter.upper()):
            print(i)
            counter += 1
            
    #if no names are found, tell the user
    if counter == 0:
        print('No last names were found starting with the letter ' + first_letter.upper())
    print()
    
#adds names to the list
def add_name():
    first = input('Enter a new first name: ')
    last = input('Enter a new last name: ')
    new_name = first + ' ' + last
    name_list.append(new_name.title())
    print(new_name.title() + ' has been added')

#removes a name from the list
def remove_name():
    remove_name = input('Enter the full name to delete: ')
    remove_name = remove_name.title()
    print()
    
    #tries to remove the name and tells the user if the name is not in the list
    try:
        name_list.remove(remove_name)
        if remove_name not in name_list:
            print(remove_name + ' has been removed')
        else:
            name_list.remove(remove_name)
            print(remove_name + ' has been removed')
    except:
        print('That name was not found')
    print()
    
#user interface for program
while True:
    print('Please select from the following options: \n')
    print('\t1. List all first names beginning with chosen letter\n\
        2. List all last names beginning with chosen letter\n\
        3  Add a name\n\
        4. Delete a name\n\
        5. Exit\n')
    
    #takes user input and starts a function based on number
    user_choice = input('Option#: ')
    if user_choice == '1':
        print()
        first_name()
    elif user_choice == '2':
        print()
        last_name()
    elif user_choice =='3':
        print()
        add_name()
    elif user_choice == '4':
        print()
        remove_name()
    elif user_choice == '5':
        break
    else:
        print('That is not a valid option. Please try again.\n')
        continue
