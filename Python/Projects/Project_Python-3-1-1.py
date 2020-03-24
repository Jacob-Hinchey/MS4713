#! python3

import os, getpass, shutil, zipfile, datetime

#sets variables for document
now = datetime.datetime.now()
for_file = now.strftime("%m_%d_%Y_")
regions = [['WA','OR', 'ID','MT', 'WY', 'CA', 'NV', 'UT', 'CO','NM','AZ'],
            ['OK','TX','AR', 'LA','MA','AL','TN','KY','WV','MD','DE','DC','VA','NC','SC','GA','FL'],
            ['ND','SD','NE','KS', 'MN','IA','MO','WI','MI','IL', 'IN','OH'],
            ['PA','NJ','NY','CT','RI','MA','VT','NH','ME']]

#Orders the active clients by state then last
def state_order(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[5][i][0].lower()<new_list[5][i-1][0].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
            elif new_list[5][i][0].lower()==new_list[5][i-1][0].lower():
                if new_list[5][i][1].lower()<new_list[5][i-1][1].lower():
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    for j in range(len(new_list)):
                        temp_list[j].append(new_list[j][i])
                        new_list[j][i] = new_list[j][i-1]
                        new_list[j][i-1] = temp_list[j][0]
                    counter+=1
        if counter ==0:
            break
    states=[]
    for i in range(len(new_list[0])-2):
        if not new_list[5][i] in states:
            states.append(new_list[5][i])
    #orders their names
    to_return=[[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(states)):
             per_state =[[],[],[],[],[],[],[],[],[],[]]
             for j in range(len(new_list[0])-2):
                 if new_list[5][j]==states[i]:
                     for k in range(len(new_list)):
                          per_state[k].append(new_list[k][j])
             while(1):
                 counter=0
                 for j in range(1,len(per_state[0]),1):
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    if per_state[1][j].lower()<per_state[1][j-1].lower():
                        for k in range(len(per_state)):
                            temp_list[k].append(per_state[k][j])
                            per_state[k][j] = per_state[k][j-1]
                            per_state[k][j-1] = temp_list[k][0]
                        counter+=1

                 if counter == 0:
                    for j in range(len(per_state)):
                        for k in range(len(per_state[0])): 
                            to_return[j].append(per_state[j][k])
                    break
    return to_return

#Orders the active clients by city then last
def city_order(new_list):
     while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[4][i].lower()<new_list[4][i-1].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
        if counter ==0:
            break
     cities=[]
     for i in range(len(new_list[0])-2):
        if not new_list[4][i] in cities:
            cities.append(new_list[4][i])
     to_return=[[],[],[],[],[],[],[],[],[],[]]
     #orders their names
     for i in range(len(cities)):
             
             per_city =[[],[],[],[],[],[],[],[],[],[]]
             for j in range(len(new_list[0])-2):
                 if new_list[4][j]==cities[i]:
                     for k in range(len(new_list)):
                          per_city[k].append(new_list[k][j])
             while(1):
                 counter=0
                 for j in range(1,len(per_city[0]),1):
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    if per_city[1][j].lower()<per_city[1][j-1].lower():
                        for k in range(len(per_city)):
                            temp_list[k].append(per_city[k][j])
                            per_city[k][j] = per_city[k][j-1]
                            per_city[k][j-1] = temp_list[k][0]
                        counter+=1

                 if counter == 0:
                    for j in range(len(per_city)):
                        for k in range(len(per_city[0])): 
                            to_return[j].append(per_city[j][k])
                    break
     return to_return

#Orders the active clients by company then last
def company_order(new_list):
     while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[9][i].lower()<new_list[9][i-1].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
        if counter ==0:
            break
     company=[]
     for i in range(len(new_list[0])-2):
        if not new_list[9][i] in company:
            company.append(new_list[9][i])
     #orders their names
     to_return=[[],[],[],[],[],[],[],[],[],[]]
     for i in range(len(company)):
             per_company =[[],[],[],[],[],[],[],[],[],[]]
             for j in range(len(new_list[0])-2):
                 if new_list[9][j]==company[i]:
                     for k in range(len(new_list)):
                          per_company[k].append(new_list[k][j])
             while(1):
                 counter=0
                 for j in range(1,len(per_company[0]),1):
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    if per_company[1][j].lower()<per_company[1][j-1].lower():
                        for k in range(len(per_company)):
                            temp_list[k].append(per_company[k][j])
                            per_company[k][j] = per_company[k][j-1]
                            per_company[k][j-1] = temp_list[k][0]
                        counter+=1

                 if counter == 0:
                    for j in range(len(per_company)):
                        for k in range(len(per_company[0])): 
                            to_return[j].append(per_company[j][k])
                    break
     return to_return

#gets the top percent of average salaries based on user input
def average_top(new_list, percentage):
     while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if float(new_list[8][i])>float(new_list[8][i-1]):
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
        if counter ==0:
            break
     new_length = int(round(len(new_list[0])*percentage,0))
     to_return=[[],[],[],[],[],[],[],[],[],[]]
     for i in range(new_length):
         for j in range(len(new_list)):
             to_return[j].append(new_list[j][i])
     return to_return

#gets salary average by state
def state_ave(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[5][i][0].lower()<new_list[5][i-1][0].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
            elif new_list[5][i][0].lower()==new_list[5][i-1][0].lower():
                if new_list[5][i][1].lower()<new_list[5][i-1][1].lower():
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    for j in range(len(new_list)-1):
                        temp_list[j].append(new_list[j][i])
                        new_list[j][i] = new_list[j][i-1]
                        new_list[j][i-1] = temp_list[j][0]
                    counter+=1
        if counter ==0:
            break
    states=[]
    for i in range(len(new_list[0])-2):
        if not new_list[5][i] in states:
            states.append(new_list[5][i])
    
    to_return=[[],[]]
    for i in range(len(states)):
        to_return[0].append(states[i])
    
    for i in range(len(states)):
        aver = []
        counter=0
        for j in range(len(new_list[0])-2):
            if states[i] == new_list[5][j]:
                aver.append(new_list[8][j])
                counter+=1
        new_flo=0.0
        for k in aver:
            new_flo+=float(k)
        new_flo=round(new_flo/counter,2)
        to_return[1].append(new_flo)
    return to_return

#gets company average salary
def company_ave(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[9][i].lower()<new_list[9][i-1].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
        if counter ==0:
            break
    states=[]
    for i in range(len(new_list[0])-2):
        if not new_list[9][i] in states:
            states.append(new_list[9][i])
    
    to_return=[[],[]]
    for i in range(len(states)-1):
        to_return[0].append(states[i])
    
    for i in range(len(states)-1):
        aver = []
        counter=0
        for j in range(len(new_list[0])-2):
            if states[i] == new_list[9][j]:
                aver.append(new_list[8][j])
                counter+=1
        new_flo=0.0
        for k in aver:
            new_flo+=float(k)
        new_flo=round(new_flo/counter,2)
        to_return[1].append(new_flo)
    return to_return

#gets average salaries of company per state
def both_ave(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[5][i][0].lower()<new_list[5][i-1][0].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
            elif new_list[5][i][0].lower()==new_list[5][i-1][0].lower():
                if new_list[5][i][1].lower()<new_list[5][i-1][1].lower():
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    for j in range(len(new_list)):
                        temp_list[j].append(new_list[j][i])
                        new_list[j][i] = new_list[j][i-1]
                        new_list[j][i-1] = temp_list[j][0]
                    counter+=1
        if counter ==0:
            break
        
    states=[]
    for i in range(len(new_list[0])-2):
        if not new_list[5][i] in states:
            states.append(new_list[5][i])
            
    company=[]
    for i in range(len(new_list[0])-2):
        if not new_list[9][i] in company:
            company.append(new_list[9][i])
            
    to_return=[[],[],[]]
    
    for i in range(len(states)-1):
        for j in range(len(company)-1):
            counter = 0
            flag = False
            aver = []
            for k in range(len(new_list[0])-2):
                if new_list[9][k] == company[j] and new_list[5][k]== states[i]:
                    aver.append(new_list[8][k])
                    flag = True
                    counter +=1
            if flag == True:
                to_return[0].append(states[i])
                to_return[1].append(company[j])
                new_flo = 0.0
                for k in aver:
                    new_flo+=float(k)
                new_flo = round(new_flo/counter,2)
                to_return[2].append(new_flo)
    return to_return
                    
#gets the ages of the clients in certain ranges
def age_bracket(new_list):
    ages = [0,0,0,0,0]
    for i in range(len(new_list[0])-2):
        new_time = datetime.datetime.strptime(new_list[7][i], '%m/%d/%Y')
        age = now.year-new_time.year
        if (now.month < new_time.month or
            (now.month == new_time.month and now.day < new_time.day)):
            age -=1
        if age < 20:
            ages[0]+=1
        elif age >=20 and age <30:
            ages[1]+=1
        elif age >=30 and age <40:
            ages[2]+=1
        elif age >=40 and age <50:
            ages[3]+=1
        else:
            ages[4]+=1
    return ages


#gets contacts sorted by state only
def contact_state(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[5][i][0].lower()<new_list[5][i-1][0].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
            elif new_list[5][i][0].lower()==new_list[5][i-1][0].lower():
                if new_list[5][i][1].lower()<new_list[5][i-1][1].lower():
                    temp_list = [[],[],[],[],[],[],[],[],[],[]]
                    for j in range(len(new_list)):
                        temp_list[j].append(new_list[j][i])
                        new_list[j][i] = new_list[j][i-1]
                        new_list[j][i-1] = temp_list[j][0]
                    counter+=1
        if counter ==0:
            break
    return new_list

#gets contacts sorted by company only
def contact_company(new_list):
    while(1):
        counter =0
        for i in range(1,len(new_list[0])-2,1):
            if new_list[9][i].lower()<new_list[9][i-1].lower():
                temp_list = [[],[],[],[],[],[],[],[],[],[]]
                for j in range(len(new_list)):
                    temp_list[j].append(new_list[j][i])
                    new_list[j][i] = new_list[j][i-1]
                    new_list[j][i-1] = temp_list[j][0]
                counter+=1
        if counter ==0:
            break
    return new_list


#gets contacts sorted by region
def contact_region(new_list):

    west_list =[[],[],[],[],[],[],[],[],[],[]]
    midwest_list =[[],[],[],[],[],[],[],[],[],[]]
    south_list =[[],[],[],[],[],[],[],[],[],[]]
    north_list =[[],[],[],[],[],[],[],[],[],[]]
    to_return = [[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(new_list[0])-2):
        for j in range(len(regions[0])-1):
            if new_list[5][i] == regions[0][j]:
                for k in range(len(new_list)):
                    west_list[k].append(new_list[k][i])
        for j in range(len(regions[1])-1):
            if new_list[5][i] == regions[1][j]:
                for k in range(len(new_list)):
                    south_list[k].append(new_list[k][i])
        for j in range(len(regions[2])-1):
            if new_list[5][i] == regions[2][j]:
                for k in range(len(new_list)):
                    midwest_list[k].append(new_list[k][i])
        for j in range(len(regions[3])-1):
            if new_list[5][i] == regions[3][j]:
                for k in range(len(new_list)):
                    north_list[k].append(new_list[k][i])
    for i in range(len(west_list[0])-1):
        for j in range(len(new_list)):
            to_return[j].append(west_list[j][i])
        to_return[10].append('West')
    for i in range(len(midwest_list[0])-1):
        for j in range(len(new_list)):
            to_return[j].append(midwest_list[j][i])
        to_return[10].append('MidWest')
    for i in range(len(south_list[0])-1):
        for j in range(len(new_list)):
            to_return[j].append(south_list[j][i])
        to_return[10].append('South')
    for i in range(len(north_list[0])-1):
        for j in range(len(new_list)):
            to_return[j].append(north_list[j][i])
        to_return[10].append('NorthEast')
    return to_return
    
    
    
            
            
#these line check to see if the dirs and files exist and creates them if they don't
user=getpass.getuser()

os.chdir('C:\\Users\\'+user+'\\Desktop\\')

if os.path.isdir('client_data'):
    if os.path.isdir('client_data\\archived_data'):
        pass
    else:
        os.mkdir('client_data\\archived_data')
    if os.path.isdir('client_data\\data_for_import'):
        pass
    else:
        os.mkdir('client_data\\data_for_import')
    if os.path.isdir('client_data\\reports'):
        pass
    else:
        os.mkdir('client_data\\reports')
    if os.path.exists('client_data\\dnc_clients.csv'):
        pass
    else:
        with open('client_data\\dnc_clients.csv','w') as f:
            f.write('First Name,Last Name,Phone,Address,City,State,Zip,DOB,Salary,Company\n')
    if os.path.exists('client_data\\active_clients.csv'):
        pass
    else:
        with open('client_data\\active_clients.csv','w') as f:
            f.write('First Name,Last Name,Phone,Address,City,State,Zip,DOB,Salary,Company')
else:
    os.mkdir('client_data')
    os.mkdir('client_data\\archived_data')
    os.mkdir('client_data\\data_for_import')
    os.mkdir('client_data\\reports')
    with open('client_data\\dnc_clients.csv','w') as f:
        f.write('First Name,Last Name,Phone,Address,City,State,Zip,DOB,Salary,Company')
    with open('client_data\\active_clients.csv','w') as f:
        f.write('First Name,Last Name,Phone,Address,City,State,Zip,DOB,Salary,Company')

os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')


#The main menu
while(1):
    print('Menu Options:\n\t1:  Import new customer data\
            \n\t2:  Add customer to Do Not Call (DNC) list\
            \n\t3:  Reports')
    user_choice = input('Please enter your choice: ') 
    if user_choice != '1' and user_choice != '2' and user_choice != '3':
            print('Please enter a valid number\n')
            continue











    #if they select to add new clients
    if user_choice == '1':
        #prompts user to move files and warns them if it is empty
        while(1):
            input('\nMove all customer data files into the '
                    +'\'data_for_import\' directory then press enter.')
            if len(os.listdir('data_for_import')) ==0:
                print('\n\'data_for_import\' is empty, please put files in there.')
                continue
            else:
                break
        #checks to see the number of files in the folder and asks the user if they
        #have asks the user if they want to add them again
        for i in os.listdir('data_for_import'):
            flag = False
            new_file =''
            for j in i:
                if j =='.':
                    break
                new_file+=j
            for j in os.listdir('archived_data'):
                zip_file=''
                for letter in j:
                    if letter =='.':
                        break
                    zip_file+=letter
                if zip_file == new_file:
                    flag = True
            if flag == True:
                print('\n' +i + ' has alrady been added before\n')
                user_in=input('Would you like to add it again. Type y if yes, and anything else for no: ')
                if user_in.lower() == 'y':
                    pass
                else:
                    continue
            #checks to see if it is a csv and throws error statement if not
            if i.endswith('.csv'):
                #loads in data from user given csv
                persons_data = [[],[],[],[],[],[],[],[],[],[]]
                with open('data_for_import\\'+i, 'r') as f:
                    for line in f:
                        j = 0
                        for k in line.split(','):
                            if j == 0:
                                first_name = k.split(' ')[0]
                                if first_name == 'Name':
                                    break
                                last_name = k.split(' ')[1]
                                persons_data[j].append(first_name)
                                persons_data[j+1].append(last_name)
                                j+=2
                                continue
                            if j==9:
                                persons_data[j].append(k.split('\n')[0])
                                continue
                            persons_data[j].append(k)
                            j+=1
                #reads current clients and stores them into list and deletes
                #person from new list if they already exist
                with open('active_clients.csv', 'r') as f:
                   temp_list = [[],[],[],[],[],[],[],[],[],[]]
                   for line in f:
                       j=0
                       for k in line.split(','):
                           if j >9:
                               break
                           temp_list[j].append(k)
                           j+=1
                   for j in range(len(persons_data[0])):
                       for k in range(len(temp_list[0])):
                           try:
                               if (persons_data[0][j] == temp_list[0][k]
                                   and persons_data[1][j] == temp_list[1][k]
                                   and persons_data[2][j] == temp_list[2][k]
                                   and persons_data[7][j] == temp_list[7][k]):
                                   for l in range(len(persons_data)):
                                       del persons_data[l][j]
                           except:
                                pass
                            
                #reads dnc clients and stores them into list and deletes
                #person from new list if they already exist
                with open('dnc_clients.csv', 'r') as f:
                   temp_list = [[],[],[],[],[],[],[],[],[],[]]
                   for line in f:
                       j=0
                       for k in line.split(','):
                           if j >9:
                               break
                           temp_list[j].append(k)
                           j+=1
                   for j in range(len(persons_data[0])):
                       for k in range(len(temp_list[0])):
                           try:
                               if (persons_data[0][j] == temp_list[0][k]
                                   and persons_data[1][j] == temp_list[1][k]
                                   and persons_data[2][j] == temp_list[2][k]
                                   and persons_data[7][j] == temp_list[7][k]):
                                   for l in range(len(persons_data)):
                                       del persons_data[l][j]
                           except:
                                pass

                #adds new clients
                with open('active_clients.csv','a') as f:
                    f.write('\n')
                    for k in range(len(persons_data[0])):
                        f.write(persons_data[0][k] + ',' +persons_data[1][k] + ',' +
                                persons_data[2][k] + ',' +persons_data[3][k] + ',' +
                                persons_data[4][k] + ',' +persons_data[5][k] + ',' +
                                persons_data[6][k] + ',' +persons_data[7][k] + ',' +
                                persons_data[8][k] + ','+persons_data[9][k]+'\n')

                #gets file name for zip and creates it if it doesn't already
                to_zip=''
                for j in i:
                    if j =='.':
                        break
                    to_zip+=j
                
                if os.path.exists('archived_data\\'+to_zip+'.zip'):
                    os.remove('data_for_import\\'+i)
                else:
                    data = zipfile.ZipFile('archived_data\\'+to_zip+'.zip','w')
                    os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\data_for_import\\')
                    data.write(i)
                    data.close()
                    os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                    os.remove('data_for_import\\'+i)

                #informs the user a file has finished processing
                print('\nFinished processing ' + i +'\n')
            else:
                print(i + ' is not a .csv so it will be skipped')










    #if user wants to add a user to dnc
    elif user_choice == '2':
        while(1):
            while(1):
                user_in= input('Enter a name or part of a name: ')
                if len(user_in)>0:
                    pass
                else:
                    print('Cannot be empty')
                if type(user_in) == str:
                    break
                else:
                    print('Cannot be an int')
            new_list = [[],[],[],[],[],[],[],[],[],[]]
            counter =0
            #reads in active clients to list if they start with the right letter 
            with open('active_clients.csv', 'r') as f:
                for line in f:
                    try:
                        if line.split(',')[0] == 'First Name':
                            continue
                        name = (line.split(',')[0]+' '+line.split(',')[1])
                        if name.upper().startswith(user_in.upper()):
                            counter+=1
                            for i in range(len(new_list)):
                                new_list[i].append(line.split(',')[i])
                    except:
                        pass
            #if no users exist, try again
            if counter ==0:
                print('No users start with that. Try again')
                continue
            #gives users a list of names and info then asks them to select a number
            #to move or q to quit
            for i in range(len(new_list[0])):
                print(str(i+1)+'. '+new_list[0][i]+' '+new_list[1][i]+', '+new_list[2][i]+', '+new_list[7][i])
            user_select=input('\nSelect a number corresponding to a name, or q to go back to first step: ')
            if user_select.lower() == 'q':
                continue
            try:
                new_list[0][int(user_select)-1]
            except:
                print('Not valid, going back to the first step')
                continue
            #displays info and asks user to confirm their selection
            print('\nUser info to be moved:\n')
            print('Name: '+new_list[0][int(user_select)-1]+' '+new_list[1][int(user_select)-1])
            print('Phone: '+ new_list[2][int(user_select)-1])
            print('Address: '+ new_list[3][int(user_select)-1])
            print('City: '+ new_list[4][int(user_select)-1])
            print('State: '+ new_list[5][int(user_select)-1])
            print('Zip Code: '+ new_list[6][int(user_select)-1])
            print('DOB: '+ new_list[7][int(user_select)-1])
            print('Salary: '+ new_list[8][int(user_select)-1])
            print('Company: '+ new_list[9][int(user_select)-1])
            print('\nAre you sure you want to move this person to the DNC list?')
            #if they say yes then add the client to dnc
            user_decide = input('Type y for yes or anything else for no: ')
            if user_decide. lower() == 'y':
                  name_to_move=new_list[0][int(user_select)-1]+' '+new_list[1][int(user_select)-1]
                  with open ('dnc_clients.csv', 'a')as f:
                      f.write(new_list[0][int(user_select)-1]+','+new_list[1][int(user_select)-1]+','+
                                  new_list[2][int(user_select)-1]+','+new_list[3][int(user_select)-1]+','+
                                  new_list[4][int(user_select)-1]+','+new_list[5][int(user_select)-1]+','+
                                  new_list[6][int(user_select)-1]+','+new_list[7][int(user_select)-1]+','+
                                  new_list[8][int(user_select)-1]+','+new_list[9][int(user_select)-1])
                  #write new active list to active_clients
                  new_active = [[],[],[],[],[],[],[],[],[],[]]
                  with open ('active_clients.csv', 'r')as f:
                      for line in f:
                          try:
                              new_name=line.split(',')[0]+' '+line.split(',')[1]
                          except:
                              continue
                          if (new_name ==name_to_move
                              and new_list[3][int(user_select)-1]==line.split(',')[3]
                              and new_list[7][int(user_select)-1]==line.split(',')[7]):
                            continue
                          if line.split(',')[0] =='Name':
                              continue
                          for i in range(len(new_active)):
                              if i == 9:
                                  to_add = line.split(',')[i]
                                  new_active[i].append(to_add.split('\n')[0])
                                  continue
                              new_active[i].append(line.split(',')[i])
                  with open ('active_clients.csv', 'w')as f:
                       f.write('First Name,Last Name,Phone,Address,City,State,Zip,DOB,Salary,Company')
                       for k in range(len(new_active[0])):
                        f.write(new_active[0][k] + ',' +new_active[1][k] + ',' +
                                new_active[2][k] + ',' +new_active[3][k] + ',' +
                                new_active[4][k] + ',' +new_active[5][k] + ',' +
                                new_active[6][k] + ',' +new_active[7][k] + ',' +
                                new_active[8][k] + ','+new_active[9][k]+'\n')
                  #asks user if they want to go again
                  print('\nWould you like to add someone else to dnc?')
                  user_again=input('Type y for yes or anything else for no: ')
                  if user_again.lower() != 'y':
                    break





    #report menu
    elif user_choice == '3':
        flag=True
        while(flag):
            print('Report Menu Options:\n\t1:  Salary Reports\n\t2:  Miscellaneous Reports\n')
            user_type= input('Please enter your choice: ')
            #gets the current client_list
            report_list=[[],[],[],[],[],[],[],[],[],[]]
            with open('active_clients.csv','r') as f:
                for line in f:
                    j = 0
                    for k in line.split(','):
                        if line.split(',')[0] == 'First Name':
                                break
                        if j==9:
                            report_list[j].append(k.split('\n')[0])
                            continue
                        report_list[j].append(k)
                        j+=1


            #Salary Repost Menu
            if user_type == '1':
                sub_flag=True
                while(sub_flag):
                     print('Salary Report Menu Options:\n\t1:  Salary by State\
                        \n\t2:  Salary by City\n\t3:  Salary by Company\
                        \n\t4:  Top % of Salaries\n\t5:  Average Salaries\n')
                     user_salary = input('Please enter your choice: ')


                     #Salary by state
                     if user_salary == '1':
                         while(1):
                             print('Would you like output to the screen, a file, or both?')
                             user_out = input('1 = screen, 2 = file, 3 = both: ')
                             
                             #print to cmd line
                             if user_out == '1':
                                  list_state= state_order(report_list)
                                  for i in range(len(list_state[0])):
                                     if list_state[5][i]!=list_state[5][i-1]:
                                         print('State: ' + list_state[5][i]+'\n')
                                     print('    '+list_state[1][i]+', '+list_state[0][i]
                                           +'\n      Salary: ' + list_state[8][i]
                                           +'\n      Company: '+list_state[9][i]+'\n')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             #prints to text file
                             elif user_out == '2':
                                  list_state= state_order(report_list)
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_State_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_State_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_state[0])):
                                        if list_state[5][i]!=list_state[5][i-1]:
                                            f.write('State: ' + list_state[5][i]+'\n\n')
                                        f.write('    '+list_state[1][i]+', '+list_state[0][i]+'\n      Salary: ' + list_state[8][i]
                                         +'\n      Company: '+list_state[9][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break

                             #prints to cmd line and file
                             elif user_out == '3':
                                  list_state= state_order(report_list)
                                  for i in range(len(list_state[0])):
                                     if list_state[5][i]!=list_state[5][i-1]:
                                         print('State: ' + list_state[5][i]+'\n')
                                     print('    '+list_state[1][i]+', '+list_state[0][i]
                                           +'\n      Salary: ' + list_state[8][i]
                                           +'\n      Company: '+list_state[9][i]+'\n')
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_State_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_State_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_state[0])):
                                        if list_state[5][i]!=list_state[5][i-1]:
                                            f.write('State: ' + list_state[5][i]+'\n\n')
                                        f.write('    '+list_state[1][i]+', '+list_state[0][i]+'\n      Salary: ' + list_state[8][i]
                                         +'\n      Company: '+list_state[9][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             else:
                                 print('\nNot a valid option\n')


                     #prints salaries by city
                     elif user_salary == '2':
                        while(1):
                             print('Would you like output to the screen, a file, or both?')
                             user_out = input('1 = screen, 2 = file, 3 = both: ')
                             
                             #print to cmd line
                             if user_out == '1':
                                  list_city= city_order(report_list)
                                  for i in range(len(list_city[0])):
                                     if list_city[4][i]!=list_city[4][i-1]:
                                         print('City: ' + list_city[4][i]+'\n')
                                     print('    '+list_city[1][i]+', '+list_city[0][i]
                                           +'\n      Salary: ' + list_city[8][i]
                                           +'\n      Company: '+list_city[9][i]+'\n')
                                  flag = False
                                  sub_flag = False
                                  break


                             #prints to text file
                             elif user_out == '2':
                                  list_city= city_order(report_list)
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_City_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_City_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_city[0])):
                                        if list_city[4][i]!=list_city[4][i-1]:
                                            f.write('City: ' + list_city[4][i]+'\n\n')
                                        f.write('    '+list_city[1][i]+', '+list_city[0][i]+'\n      Salary: ' + list_city[8][i]
                                         +'\n      Company: '+list_city[9][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break

                             #prints to cmd line and file
                             elif user_out == '3':
                                  list_city= city_order(report_list)
                                  for i in range(len(list_city[0])):
                                     if list_city[4][i]!=list_city[4][i-1]:
                                         print('City: ' + list_city[4][i]+'\n')
                                     print('    '+list_city[1][i]+', '+list_city[0][i]
                                           +'\n      Salary: ' + list_city[8][i]
                                           +'\n      Company: '+list_city[9][i]+'\n')
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_City_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_City_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_city[0])):
                                        if list_city[4][i]!=list_city[4][i-1]:
                                            f.write('City: ' + list_city[4][i]+'\n\n')
                                        f.write('    '+list_city[1][i]+', '+list_city[0][i]+'\n      Salary: ' + list_city[8][i]
                                         +'\n      Company: '+list_city[9][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             else:
                                 print('\nNot a valid option\n')


                     #prints salaries by company
                     elif user_salary == '3':
                         while(1):
                             print('Would you like output to the screen, a file, or both?')
                             user_out = input('1 = screen, 2 = file, 3 = both: ')
                             
                             #print to cmd line
                             if user_out == '1':
                                  list_company= company_order(report_list)
                                  for i in range(len(list_company[0])):
                                     if list_company[9][i]!=list_company[9][i-1]:
                                         print('Company: ' + list_company[9][i]+'\n')
                                     print('    '+list_company[1][i]+', '+list_company[0][i]
                                           +'\n      Salary: ' + list_company[8][i]+'\n')
                                  flag = False
                                  sub_flag = False
                                  break


                             #prints to text file
                             elif user_out == '2':
                                  list_company= company_order(report_list)
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_Company_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_Company_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_company[0])):
                                        if list_company[9][i]!=list_company[9][i-1]:
                                            f.write('Company: ' + list_company[9][i]+'\n\n')
                                        f.write('    '+list_company[1][i]+', '+list_company[0][i]
                                                +'\n      Salary: ' + list_company[8][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             #prints to cmd line and file
                             elif user_out == '3':
                                  list_company= company_order(report_list)
                                  for i in range(len(list_company[0])):
                                     if list_company[9][i]!=list_company[9][i-1]:
                                         print('Company: ' + list_company[9][i]+'\n')
                                     print('    '+list_company[1][i]+', '+list_company[0][i]
                                           +'\n      Salary: ' + list_company[8][i]+'\n')
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Sal_by_Company_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Sal_by_Company_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     for i in range(len(list_company[0])):
                                        if list_company[9][i]!=list_company[9][i-1]:
                                            f.write('Company: ' + list_company[9][i]+'\n\n')
                                        f.write('    '+list_company[1][i]+', '+list_company[0][i]
                                                +'\n      Salary: ' + list_company[8][i]+'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             else:
                                 print('\nNot a valid option\n')



                     #print percentage of top salaries given by user
                     elif user_salary == '4':
                         while(1):
                             #GET USER PERCENTAGE AS a number
                             percentage = input('What percentage of salaries would you like?: ')
                             #check to make sure it is valid and convert it
                             try:
                                 percentage = float(percentage)
                             except:
                                 print('Enter a number only')
                                 continue
                             if percentage >99.99:
                                 print('percentage must be less than 100')
                             elif percentage < .0001:
                                 print('percentage must be greater than 0')
                             percentage = round(percentage/100, 2)
                             list_average= average_top(report_list,percentage)
                             print('Would you like output to the screen, a file, or both?')
                             user_out = input('1 = screen, 2 = file, 3 = both: ')
                             
                             #print to cmd line
                             if user_out == '1':
                                  print('Top ' +str(percentage*100)+ '% of salaries\n')
                                  for i in range(len(list_average[0])):
                                     print(list_average[1][i]+', '+list_average[0][i]
                                           +'\n    Company: '+ list_average[9][i]
                                           +'\n    Salary: ' + list_average[8][i]
                                           +'\n')
                                  flag = False
                                  sub_flag = False
                                  break
                                
                             #prints to text file
                             elif user_out == '2':
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Top_average_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Top_average_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     f.write('Top ' +str(percentage*100)+ '% of salaries\n\n')
                                     for i in range(len(list_average[0])):
                                        f.write(list_average[1][i]+', '+list_average[0][i]
                                                +'\n      Company: ' + list_average[9][i]
                                                +'\n      Salary: ' + list_average[8][i]
                                                +'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break

                             #prints to cmd line and file
                             elif user_out == '3':
                                  print('Top ' +str(percentage*100)+ '% of salaries\n')
                                  for i in range(len(list_average[0])):
                                     print(list_average[1][i]+', '+list_average[0][i]
                                           +'\n    Company: '+ list_average[9][i]
                                           +'\n    Salary: ' + list_average[8][i]
                                           +'\n')
                                  #checks file names available
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                  new_filename=''
                                  for i in range(10000):
                                     if os.path.exists('Top_average_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Top_average_'+for_file+str(i)+'.txt'
                                     break
                                  with open(new_filename,'w') as f:
                                     f.write('Top ' +str(percentage*100)+ '% of salaries\n\n')
                                     for i in range(len(list_average[0])):
                                        f.write(list_average[1][i]+', '+list_average[0][i]
                                                +'\n      Company: ' + list_average[9][i]
                                                +'\n      Salary: ' + str(list_average[8][i])
                                                +'\n')
                                        f.write('\n')
                                  os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                  flag = False
                                  sub_flag = False
                                  break
                             else:
                                 print('\nNot a valid option\n')


                     #Salaries by company, state, or both
                     elif user_salary == '5':
                         flag_again=True
                         while(flag_again):
                             while(1):
                                 print('Would you like to group by company state or both?')
                                 user_outer = input('1 = company, 2 = state, 3 = both: ')
                                 if user_outer !='1' and user_outer!='2' and user_outer!='3':
                                     print('Not a valid option')
                                     continue
                                 print('Would you like output to the screen, a file, or both?')
                                 user_out = input('1 = screen, 2 = file, 3 = both: ')

                                 #pprint to cmd line
                                 if user_out == '1':
                                      
                                      #averge salary by company
                                      if user_outer == '1':
                                          list_by = company_ave(report_list)
                                          for i in range(len(list_by[0])):
                                              print('\nCompany: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i]))
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          break

                                      #average salary by state
                                      elif user_outer == '2':
                                          list_by = state_ave(report_list)
                                          for i in range(len(list_by[0])):
                                              print('\nState: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i]))
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          break
                                        
                                      #average salary by both state and compnay
                                      elif user_outer == '3':
                                          list_by = both_ave(report_list)
                                          
                                          for i in range(len(list_by[0])):
                                              if list_by[0][i] != list_by[0][i-1]:
                                                  print('\nState: ' + list_by[0][i])
                                              print('   Company: ' +list_by[1][i]
                                                    +'\n      Average Salary: '
                                                    +str(list_by[2][i])+'\n')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          break
                                      else:
                                        print('\nNot a valid option\n')

                                 #prints to text file
                                 elif user_out == '2':
                                     
                                      #averge salary by company
                                      if user_outer == '1':
                                          list_by = company_ave(report_list)
                                          
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_company_'+for_file+str(i)+'.txt'):
                                                continue
                                             new_filename = 'Sal_by_company_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                              for i in range(len(list_by[0])):
                                                  f.write('\nCompany: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i])+'\n')

                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          break

                                      #average salary by state
                                      elif user_outer == '2':
                                          list_by = state_ave(report_list)
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_state_'+for_file+str(i)+'.txt'):
                                                continue
                                            
                                             new_filename = 'Sal_by_state_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                              for i in range(len(list_by[0])):
                                                  f.write('\nState: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i])+'\n')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          break

                                      #average salary by both state and compnay
                                      elif user_outer == '3':
                                          list_by = both_ave(report_list)
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_State_and_Company_'+for_file+str(i)+'.txt'):
                                                continue
                                             new_filename = 'Sal_by_State_and_Company_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                             for i in range(len(list_by[0])):
                                                if list_by[0][i] != list_by[0][i-1]:
                                                   f.write('\n')
                                                   f.write('State: ' + list_by[0][i]+'\n')
                                                f.write('   Company: ' +list_by[1][i]
                                                    +'\n      Average Salary: '
                                                    +str(list_by[2][i])+'\n')
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          break
                                      else:
                                        print('\nNot a valid option\n')
                                        
                                 #print to cmd line and file
                                 elif user_out == '3':

                                      #average salary by company
                                      if user_outer == '1':
                                          list_by = company_ave(report_list)
                                          for i in range(len(list_by[0])):
                                              print('\nCompany: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i]))
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_company_'+for_file+str(i)+'.txt'):
                                                continue
                                             new_filename = 'Sal_by_company_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                              for i in range(len(list_by[0])):
                                                  f.write('\nCompany: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i])+'\n')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          break

                                      #average salary by state
                                      elif user_outer == '2':
                                          list_by = state_ave(report_list)
                                          for i in range(len(list_by[0])):
                                              print('\nState: ' + list_by[0][i]+'\n    Average Salary: ' +str(list_by[1][i]))
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_state_'+for_file+str(i)+'.txt'):
                                                continue
                                             new_filename = 'Sal_by_state_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                              for i in range(len(list_by[0])):
                                                  f.write('\nState: ' + list_by[0][i]
                                                          +'\n      Average Salary: ' +str(list_by[1][i])+'\n')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          break
                                        
                                      #average salary by both state and compnay
                                      elif user_outer == '3':
                                          list_by = both_ave(report_list)
                                          for i in range(len(list_by[0])):
                                              if list_by[0][i] != list_by[0][i-1]:
                                                  print('\nState: ' + list_by[0][i])
                                              print('   Company: ' +list_by[1][i]
                                                    +'\n      Average Salary: '
                                                    +str(list_by[2][i])+'\n')
                                          #checks file names available
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                          new_filename=''
                                          for i in range(10000):
                                             if os.path.exists('Sal_by_State_and_Company_'+for_file+str(i)+'.txt'):
                                                continue
                                             new_filename = 'Sal_by_State_and_Company_'+for_file+str(i)+'.txt'
                                             break
                                          with open(new_filename,'w') as f:
                                             for i in range(len(list_by[0])):
                                                if list_by[0][i] != list_by[0][i-1]:
                                                   f.write('\n')
                                                   f.write('State: ' + list_by[0][i]+'\n')
                                                f.write('   Company: ' +list_by[1][i]
                                                    +'\n      Average Salary: '
                                                    +str(list_by[2][i])+'\n')
                                          os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                          flag = False
                                          sub_flag = False
                                          flag_again=False
                                          break
                                      else:
                                        print('\nNot a valid option\n')
                                 else:
                                     print('\nNot a valid option\n')

                                 
                     else:
                          print('\nNot a valid option\n')
                          continue



            #miscallaneous reports menu
            if user_type =='2':
                flag_again = True
                while(flag_again):
                     print('Miscallaneous Report Menu Options:\n\t1:  Customer Age Brackets\
                        \n\t2:  Contact List\n')
                     user_misc = input('Please enter your choice: ')
                     
                     #Customer age brackets
                     if user_misc == '1':
                         while(1):
                             print('Would you like output to the screen, a file, or both?')
                             user_out = input('1 = screen, 2 = file, 3 = both: ')
                             
                             #print to cmd line
                             if user_out == '1':
                                 age_list = age_bracket(report_list)
                                 for i in range(len(age_list)):
                                     age_list[i] = str(age_list[i])
                                 print('Clients younger than 20: '+age_list[0]
                                       +'\nClients 20 or older and less than 30: '+ age_list[1]
                                       +'\nClients 30 or older and less than 40: '+ age_list[2]
                                       +'\nClients 40 or older and less than 50: '+ age_list[3]
                                       +'\nClients 50 or older: '+ age_list[4])
                                 flag = False
                                 sub_flag = False
                                 flag_again=False
                                 break
                                
                             #prints to text file
                             elif user_out == '2':
                                 age_list = age_bracket(report_list)
                                 for i in range(len(age_list)):
                                     age_list[i] = str(age_list[i])
                                 #checks file names available
                                 os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                 new_filename=''
                                 for i in range(10000):
                                     if os.path.exists('Age_brackets_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Age_brackets_'+for_file+str(i)+'.txt'
                                     break
                                 with open(new_filename,'w') as f:
                                     f.write('Clients younger than 20: '+age_list[0]
                                       +'\nClients 20 or older and less than 30: '+ age_list[1]
                                       +'\nClients 30 or older and less than 40: '+ age_list[2]
                                       +'\nClients 40 or older and less than 50: '+ age_list[3]
                                       +'\nClients 50 or older: '+ age_list[4]+'\n')

                                 os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                 flag = False
                                 sub_flag = False
                                 flag_again=False
                                 break
                                
                             #prints to cmd line and file
                             elif user_out == '3':
                                 age_list = age_bracket(report_list)
                                 for i in range(len(age_list)):
                                     age_list[i] = str(age_list[i])

                                 print('Clients younger than 20: '+age_list[0]
                                       +'\nClients 20 or older and less than 30: '+ age_list[1]
                                       +'\nClients 30 or older and less than 40: '+ age_list[2]
                                       +'\nClients 40 or older and less than 50: '+ age_list[3]
                                       +'\nClients 50 or older: '+ age_list[4])
                                 #checks file names available
                                 os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                 new_filename=''
                                 for i in range(10000):
                                     if os.path.exists('Age_brackets_'+for_file+str(i)+'.txt'):
                                        continue
                                     new_filename = 'Age_brackets_'+for_file+str(i)+'.txt'
                                     break
                                 with open(new_filename,'w') as f:
                                     f.write('Clients younger than 20: '+age_list[0]
                                       +'\nClients 20 or older and less than 30: '+ age_list[1]
                                       +'\nClients 30 or older and less than 40: '+ age_list[2]
                                       +'\nClients 40 or older and less than 50: '+ age_list[3]
                                       +'\nClients 50 or older: '+ age_list[4]+'\n')
                                 os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                 flag = False
                                 sub_flag = False
                                 flag_again=False
                                 break
                             else:
                                 print('\nNot a valid option\n')



                     #contact List Report Menu
                     elif user_misc == '2':
                          print('Contact List Report Menu Options:\n\t1:  By State\
                            \n\t2:  By Company\n\t3:  By Region\n')
                          user_contact = input('Please enter your choice: ')

                          #STATE report list
                          if user_contact == '1':
                             while(1):
                                 print('Would you like output to the screen, a file, or both?')
                                 user_out = input('1 = screen, 2 = file, 3 = both: ')
                                 #print to cmd line
                                 if user_out == '1':
                                     new_list = contact_state(report_list)
                                     for i in range(len(new_list[0])-2):
                                         if new_list[5][i]!=new_list[5][i-1]:
                                             print('State: ' + new_list[5][i]+'\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break
                                
                                 #prints to text file
                                 elif user_out == '2':
                                     new_list = contact_state(report_list)
                                     #checks file names available
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_State_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_State_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                                             if new_list[5][i]!=new_list[5][i-1]:
                                                f.write('\nState: ' + new_list[5][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 #prints to cmd line and file
                                 elif user_out == '3':
                                     new_list = contact_state(report_list)
                                     for i in range(len(new_list[0])-2):
                                         if new_list[5][i]!=new_list[5][i-1]:
                                             print('State: ' + new_list[5][i]+'\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     #checks file names available
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_State_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_State_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                                             if new_list[5][i]!=new_list[5][i-1]:
                                                f.write('\nState: ' + new_list[5][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 else:
                                     print('\nNot a valid option\n')

                          #company contact list
                          elif user_contact == '2':
                             while(1):
                                 print('Would you like output to the screen, a file, or both?')
                                 user_out = input('1 = screen, 2 = file, 3 = both: ')
                                 
                                 #print to cmd line
                                 if user_out == '1':
                                     new_list = contact_company(report_list)
                                     for i in range(len(new_list[0])-2):
                                         if new_list[9][i]!=new_list[9][i-1]:
                                             print('Company: ' + new_list[9][i]+'\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 #prints to text file
                                 elif user_out == '2':
                                     new_list = contact_company(report_list)
                                     #checks file names available
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_Company_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_Company_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                
                                             if new_list[9][i]!=new_list[9][i-1]:
                                                f.write('\nCompany: ' + new_list[9][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 #prints to cmd line and file
                                 elif user_out == '3':
                                     new_list = contact_company(report_list)
                                     for i in range(len(new_list[0])-2):
                                         if new_list[9][i]!=new_list[9][i-1]:
                                             print('Company: ' + new_list[9][i]+'\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     #checks file names available
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_Company_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_Company_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                
                                             if new_list[9][i]!=new_list[9][i-1]:
                                                f.write('\nCompany: ' + new_list[9][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break
                                 else:
                                     print('\nNot a valid option\n')




                          #contact list by region
                          elif user_contact == '3':
                             while(1):
                                 print('Would you like output to the screen, a file, or both?')
                                 user_out = input('1 = screen, 2 = file, 3 = both: ')
                                 
                                 #print to cmd line
                                 if user_out == '1':
                                     new_list = contact_region(report_list)
                                     print('West:\n')
                                     for i in range(len(new_list[1])-2):
                                         if new_list[10][i] != new_list[10][i-1]:
                                             print('\nRegion: '+new_list[10][i]+':\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 #prints to text file
                                 elif user_out == '2':
                                     new_list = contact_region(report_list)
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     #checks file names available
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_Region_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_Region_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                                             if new_list[10][i]!=new_list[10][i-1]:
                                                f.write('\nRegion: ' + new_list[10][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break
                                     
                                 #prints to cmd line and file
                                 elif user_out == '3':
                                     new_list = contact_region(report_list)
                                     print('West:\n')
                                     for i in range(len(new_list[1])-2):
                                         if new_list[10][i] != new_list[10][i-1]:
                                             print('\n'+new_list[10][i]+':\n')
                                         print('    '+new_list[1][i]+', '+new_list[0][i]
                                               +'\n      Phone: ' + new_list[2][i]
                                               +'\n      Address: '+ new_list[3][i] +', '
                                               +new_list[4][i]+', '+new_list[5][i] + ', '
                                               +new_list[6][i]
                                               +'\n      Company: '+new_list[9][i]+'\n')
                                     #checks file names available
                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\reports\\')
                                     new_filename=''
                                     for i in range(10000):
                                         if os.path.exists('Contact_by_Region_'+for_file+str(i)+'.txt'):
                                            continue
                                         new_filename = 'Contact_by_Region_'+for_file+str(i)+'.txt'
                                         break
                                     with open(new_filename,'w') as f:
                                         for i in range(len(new_list[0])-2):
                                             if new_list[10][i]!=new_list[10][i-1]:
                                                f.write('\nRegion: ' + new_list[10][i]+'\n')
                                             f.write('\n    '+new_list[1][i]+', '+new_list[0][i]
                                                       +'\n      Phone: ' + new_list[2][i]
                                                       +'\n      Address: '+ new_list[3][i] +', '
                                                       +new_list[4][i]+', '+new_list[5][i] + ', '
                                                       +new_list[6][i]
                                                       +'\n      Company: '+new_list[9][i]+'\n')

                                     os.chdir('C:\\Users\\'+user+'\\Desktop\\client_data\\')
                                     flag = False
                                     sub_flag = False
                                     flag_again=False
                                     break

                                 else:
                                     print('\nNot a valid option\n')
                          else:
                              print('\nNot a valid option\n')
                              continue

            #if not a valid input
            elif user_type != '1' and user_type !='2':       
                print('\nNot a valid option\n')
                continue
            print('\n')






















        











    
