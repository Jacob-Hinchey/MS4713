#! python3

import os
import getpass
import shutil
import sys

#used to create folders
abcs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#makes ps_scripts dir and alphabet folders
def makeDir():
    os.mkdir('C:\\Users\\'+user+'\\Desktop\\ps_scripts')
    for i in abcs:
        os.mkdir('C:\\Users\\'+user+'\\Desktop\\ps_scripts\\'+i)

#copies .ps1 files to their correct folder
def putIn(fileT):
    #checks to see if first letter matches dir name
    for i in abcs:
        if fileT.startswith(i):
            toCop = str('C:\\Users\\'+user+'\\Desktop\\ps_scripts\\'+i)
            #makes sure no file with the same name already exists
            try:
                shutil.copy(fileT, toCop)
            except:
                pass
                

        
#gets user name for paths
user = getpass.getuser()
os.chdir('C:')

#deletes the folder if it already exists
if os.path.isdir('C:\\Users\\'+user+'\\Desktop\\ps_scripts'):
    shutil.rmtree('C:\\Users\\'+user+'\\Desktop\\ps_scripts')
    
#calls make dir and assigns default dir
makeDir()
os.chdir('C:\\Users\\'+user+'\\Desktop\\ps_scripts\\')

#walks the C: drive
for folder_name, subfolder, filename in os.walk('C:\\'):
    #try is for campus computers in case access is not provided
    try:
        os.chdir(folder_name)
    except:
        pass

    #checks each file to see if it ends in .ps1 and calls the copy function if it does
    for i in filename:
        if i.endswith('.ps1'):
            putIn(i)
        else:
            continue

#walks the ps_scripts folder to get file count and sizes
count =0
totalSize = 0.0
for folder_name, subfolder, filename in os.walk('C:\\Users\\'+user+'\\Desktop\\ps_scripts\\'):
    for i in filename:
        totalSize += os.path.getsize(os.path.join(folder_name, i))
        count+=1

#prints to commandline
input(str(count)+' files were copied for a total of approximately '+str(round(totalSize/1000000,2))+' GB')

