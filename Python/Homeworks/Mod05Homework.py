#! python3

#This is my original dictionary of events
events={
'Weezer': {'Jan 30, 2018': ['Concrete Gold', 'Etihad Stadium', 'Melbourne, VIC'],
           'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina',  'Montebello, QC']},
'Tenacious D': {'May 06, 2018': ['Shaky Knees Music Festival 2018', 'Central Park', 'Atlanta, GA'],
                'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
'Lamb of God': {'Jun 09, 2018': ['Final World Tour: North America 2018', 'Keybank Pavilion', 'Burgettstown, PA'],
                'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
'Ed Sheeran': {'Mar 10, 2018': ['Ed Sheeran with Missy Higgins', 'Etihad Stadium', 'Melbourne, VIC']},
'Cold War Kids': {'Jun 02, 2018': ['XFEST 2018', 'Keybank Pavilion', 'Burgettstown, PA']},
'Steel Panther': {'Oct 21, 2017': ['Aftershock', 'Discovery Park', 'Sacramento, CA']}}
#iterates through the dictioaries and list to print them
def print_events():
    print()
    for i in events:
        print(i)
        for j in events[i]:
            print('\t' + j)
            for k in events[i][j]:
                print('\t\t' + k)

#Takes input from the user and adds it to the current events dictionary
def add_event():
    while True:
        
        #get user input
        artist_or_band = input('\nArtist or Band: ')
        concert = input('Concert: ')
        date = input('Date: ')
        venue = input('Venue: ')
        location = input('Location: ')

        #insert a new band or just new information
        if artist_or_band in events:
            #used updates since adding items does not work in python3
            events[artist_or_band].update({date: [concert, venue, location]})
        else:
             events.update({artist_or_band: {date: [concert, venue, location]}})
            #ask user if they want to add more
        user_in = input('\nQ to stop entering new concerts, anything else to add more concerts: ')
        user_in = user_in.upper()
        if user_in == 'Q':
                break
print_events()

#loops takes user input and adds event if the user wants to
while True:
    #ask user if they want to add an event and
    user_choice = input('\nEnter Y if you would like to add more events or hit eneter to quit: ')
    user_choice = user_choice.upper()

    if user_choice == 'Y':
        add_event()
        print_events()

    else:
        break
    
input()
