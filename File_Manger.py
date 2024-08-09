import os 
import sys
import shutil

Value = str("A")
Value = input("Hello to Fernados file manager if you want your files managed press Z ")

if Value == "Z":
    print("You have decided to continue")
else:  
    sys.exit("Thank you for not pressing Z who saved me from writing a bunch of lines")


list_folders = ["Pictures Folder", "Videos_Folder", "EXE folder" ,"TXT_Folder", "Jpg_Folder", "Png_Folder", "MP4_folder", "MP3_folder", "Wav_Folder", "Junk_Items"]

for item in list_folders:  
    newpath = rf"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\{item}"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

file_names = os.listdir("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items")

print(file_names[0])

#for True_files in file_names:
    # number = 0 
    # file_names[number] = True_files
    # number + 1
    # True_files == True_files.split
    # print(True_files)

for placment in file_names:
    if file_names.endswith == ".exe":
        shutil.move(file_names)