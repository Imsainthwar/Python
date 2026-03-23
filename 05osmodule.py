import os

# Specify the Directory you want to list 
directory_path = 'D:\Book\Gate'

#List all the files and directory in the specified path
contents = os.listdir(directory_path)

#Print Each file and Directory name
for item in contents:
    print(item)