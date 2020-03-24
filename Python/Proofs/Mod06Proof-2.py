#! python3

import os
import getpass
import shutil

#reverses a string
def reverse_it(flipIt):
    to_reverse = ''
    for i in range(4,-1,-1) :
        to_reverse += flipIt[i]
    return to_reverse

user = getpass.getuser()
os.chdir('C:')

#deletes the folders if they already exists
if os.path.isdir('C:\\Users\\'+user+'\\Desktop\\dirbyalpha'):
    shutil.rmtree('C:\\Users\\'+user+'\\Desktop\\dirbyalpha')
if os.path.isdir('C:\\Users\\'+user+'\\Desktop\\revfilebyalpha'):
    shutil.rmtree('C:\\Users\\'+user+'\\Desktop\\revfilebyalpha')

#makes necassary dirs
os.mkdir('C:\\Users\\'+user+'\\Desktop\\dirbyalpha')
os.mkdir('C:\\Users\\'+user+'\\Desktop\\revfilebyalpha')

#Task1
#holds paths
paths_list =[]
dir_in_tiny=0
#iterates through tinyfiles backwards
for folder_name, subfolder, filename in os.walk('C:\\Users\\'+user+'\\Desktop\\tinyfiles', topdown =False):
    
    #adds paths to the lists
    for i in filename:
        new_path = folder_name+'\\'+ i
        paths_list.append(new_path)
        os.rename(folder_name +'\\' + i, folder_name+'\\'+i.lower())
        
    #iterates through folders and assigns them to a letter file in dirbyalpha
    for i in subfolder:
        dir_in_tiny+=1
        os.rename(folder_name+'\\'+i, folder_name+'\\'+i.upper())
        letter=i[0].upper()

        #if folder already exists add the dir if not create a letter dir then add it
        if os.path.isdir('C:\\Users\\'+user+'\\Desktop\\dirbyalpha\\'+letter):
            pass
        else:
            os.mkdir('C:\\Users\\'+user+'\\Desktop\\dirbyalpha\\'+letter)
        shutil.move(folder_name+'\\'+i.upper(), 'C:\\Users\\'+user+'\\Desktop\\dirbyalpha\\'+letter)

print('Directories in tinyfiles: '+str(dir_in_tiny))
dir_in_new=0

#number of dir in dirbyalpha
for folder_name, subfolder, filename in os.walk('C:\\Users\\'+user+'\\Desktop\\dirbyalpha'):
    for i in subfolder:
        dir_in_new +=1
        
input('Directories in dirbyalpha: '+str(dir_in_new))

#Task2
os.chdir('C:\\Users\\'+user+'\\Desktop\\revfilebyalpha')

#adds files from dirbyalpha to revfilebyalpha with backwards names
for folder_name, subfolder, filename in os.walk('C:\\Users\\'+user+'\\Desktop\\dirbyalpha'):
    for i in filename:
        pat = folder_name+'\\'+i
        shutil.copy(pat, reverse_it(i)+'.txt')

#Task3
while(True):
    #takes usr input and makes sure it's a letter
    user_input = input('Give me a letter: ') 
    try:
        user_input = user_input.lower()
        if(len(user_input)==1 and user_input.isalpha()):
            break
        print('Please enter a letter only!')
    except:
        print('Please enter a letter only!')

#scans dirbyalpha to find files beginning with a user given letter
for folder_name, subfolder, filename in os.walk('C:\\Users\\'+user+'\\Desktop\\dirbyalpha'): 
    for i in filename:
        #finds files
        if i.startswith(user_input):
            path_to_print = ''
            size = os.path.getsize(os.path.join(folder_name, i))
            #finds the original path(with original caps and file
            #name before lowercase or caps) of the file in tinyfiles
            for j in paths_list:
                if j.lower().endswith(i.lower()):
                    path_to_print = j
                    break
            print('\nFilename: ' + i + '\nSize in bytes: '+ str(size) + '\nOriginal path: ' +path_to_print)
            

#Task4
#tries to delete tinyfiles
try:
    shutil.rmtree('C:\\Users\\'+user+'\\Desktop\\tinyfiles')
    print('\ntinyfiles deleted!')
except:
    print('\nCould not delete tinyfiles.')

input()
