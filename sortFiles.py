# Created by Vaishak Murali on 06-Nov-2017. This python code is used to sort files in to it's particular folder. 
import os
import shutil

def Folders(extension):
    # This function is used to create folder name from extension.  
    folderName = None
    for i in extension.__len__():
        if i ==".":
            continue
        else:
            folderName = extension[i]
    return folderName

def main():
    # Listing all the files in current working directory. 
    files = os.listdir(".") 

    # Loop to sort files in current working directory.
    for i in files:

        # Condition to avoid folders to be read.
        if i.startswith(".") or os.path.isdir(i):
            continue

            # This condition will run if it is fetching files.
        else:
            
            # Fetching extention of the file.
            
            #grd Edit - no need of extension. Redundant.
            #extension = os.path.splitext(i)[1]
            folderName = i.split(".")[1]

            # Sorting the files in respective folder if it exists.
            if os.path.exists(folderName):
                shutil.move(i, folderName)

            # Sorting the files in respective folder if it does not exists. In this case we will create a new folder.    
            else:
                os.mkdir(folderName)
                shutil.move(i, folderName)
main()
