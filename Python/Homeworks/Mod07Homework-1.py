#! python3
import os
import getpass

#setpath
user = getpass.getuser()
os.chdir('C:\\Users\\'+user+'\\Desktop\\')

#create lists for data
prior_list =[]
class_list =[]
description_list =[]
source_list =[]
destination_list =[]

#max length variables
priority_max =0
class_max =0
description_max =0
source_ip_max =0
destination_ip_max =0
total_rows=0

#read in from the wireshark file
with open('alert.fast.maccdc2012_00000.pcap','r') as f:
    for line in f:
        
        #stores priorities into a list
        priority =  line.split(': ')[2]
        priority_list = priority.split(']')[0]
        #print(priority_list)
        priority_list=priority_list.rstrip()
        prior_list.append(priority_list)
        if len(priority_list) > priority_max:
            priority_max = len(priority_list)

        #stores classification into a list
        classif =  line.split(': ')[1]
        classif_list = classif.split(']')[0]
        #print(classif_list))
        classif_list=classif_list.rstrip()
        class_list.append(classif_list)
        if len(classif_list) > class_max:
            class_max = len(classif_list)

        #stores description into a list
        desc =line.split('] ')[2]
        desc_list = desc.split('[')[0]
        #print(desc_lis)
        desc_list = desc_list.replace(',',';')
        desc_list=desc_list.rstrip()
        description_list.append(desc_list)
        if len(desc_list) > description_max:
            description_max = len(desc_list)

        #stores source ip into a list
        sip =  line.split('} ')[1]
        sip_list = sip.split('-')[0]
        #print(sip_list)
        sip_list=sip_list.rstrip()
        source_list.append(sip_list)
        if len(sip_list) > source_ip_max:
            source_ip_max = len(sip_list)

        #stores destination ip into a list
        dips =  line.split('> ')[1]
        dip = dips.split('\n')[0]
        #print(dip)
        dip=dip.rstrip()
        destination_list.append(dip)
        if len(dip) > destination_ip_max:
            destination_ip_max = len(dip)
        
        #count rows
        total_rows+=1

#insert these new list into their resepctive columns
with open('alert_data.csv','w') as f:
    f.write('Priority,Classification,Description,Source IP,Destination IP,\n')
    for i in range(len(prior_list)):
        f.write(prior_list[i] + ',' +
                class_list[i] + ',' +
                description_list[i] + ',' +
                source_list[i] + ',' +
                destination_list[i] + ',\n')
        

#print the necassary info
print('Maximum Field Length\n\nPriority: ' + str(priority_max)
      + '\nClassification: '+str(class_max)+'\nDescription: '+str(description_max)
      + '\nSource IP: '+str(source_ip_max)+'\nDestination IP: '+str(destination_ip_max))
print('\nExcluding the column header there are '+str(total_rows)+' rows of data.')
input()
