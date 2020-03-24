#! python3

import os
import getpass
import shutil
import sys
import zipfile

abcs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

user = getpass.getuser()
os.chdir('C:\\Users\\'+user+'\\Desktop\\')
#check ifdir is amde and make it with a through z zips
if os.path.isdir('zipbyfirstletter'):
    shutil.rmtree('zipbyfirstletter')
os.mkdir('zipbyfirstletter')
os.chdir('C:\\Users\\'+user+'\\Desktop\\zipbyfirstletter')
for i in abcs:
    newzip = zipfile.ZipFile(i+'.zip', 'w')
    newzip.close()
os.chdir('C:\\Users\\'+user+'\\Desktop\\')

#interate through tiny files
for folder_name, subfolder, filename in os.walk('tinyfiles'):
    for i in filename:
        first_letter=''
        #gets the first letter of each file content
        with open(folder_name+'\\'+i, 'r') as f:
            count = 0
            for line in f:
                if count ==0:
                    first_letter = line[0]
                count+=1
        os.chdir(folder_name+'\\')
        #puts files into their correct zip
        for j in abcs:
            if first_letter.upper() == j:
                data = zipfile.ZipFile('C:\\Users\\'+user+'\\Desktop\\zipbyfirstletter\\'+j+'.zip', 'a')
                data.write(i, compress_type=zipfile.ZIP_DEFLATED)
                data.close()
        os.chdir('C:\\Users\\'+user+'\\Desktop\\')

os.chdir('C:\\Users\\'+user+'\\Desktop\\')

#interated through the alphabet
for i in abcs:
    #things to print
    name_zips=i+'.zip'
    size=0
    files=0
    #open each zip file and interate through it to get its size and the files in it
    zipread = zipfile.ZipFile('C:\\Users\\'+user+'\\Desktop\\zipbyfirstletter\\'+i+'.zip')
    for j in zipread.infolist():
        files+=1
        size += j.file_size
    size = round(size/1000, 2)
    #use file_size, compres_size, or the average of them does not return the
    #value you had
    print('Archives Name: '+name_zips +'\nArchive size: ' +str(size)+ ' KB\n'
          + name_zips +' containss '+str(files)+' compressed files\n')
    zipread.close()
input()
