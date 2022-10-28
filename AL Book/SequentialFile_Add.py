import sys
import glob
import os.path

list_of_files = glob.glob('/Users/Emily/Topics/*.txt') #500 files

for file_name in list_of_files:
    print(file_name)

    # This needs to be done *inside the loop*
    f= open(file_name, 'r')
    lst = []
    for line in f:
       line.strip()
       line = line.replace("\n" ,'')
       line = line.replace("//" , '')
       lst.append(line)
    f.close()

    f=open(os.path.join('/Users/Emily/UpdatedTopics',
    os.path.basename(file_name)) , 'w')

    for line in lst:
       f.write(line)
    f.close()