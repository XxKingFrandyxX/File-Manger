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



# for True_files in file_names:
#      number = 0 
#      file_names[number] = True_files
#      number + 1
#      if number == "":
#          break
True_files = None
         
for placment in file_names:
    number = 0
    file_names[number] = True_files
    True_files = str(True_files)
    print (True_files)
    if True_files.endswith == ".exe":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\EXE folder\\" + {file_names})
    if True_files.endswith == ".txt":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\TXT_Folder\\" + {file_names})
    if True_files.endswith == ".png":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Pictures Folder\\" + {file_names})
    if True_files.endswith == ".mp4":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Vidoes_Folder\\" + {file_names})
    if True_files.endswith == ".jpg":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Jpg_Folder\\" + {file_names})
    if True_files.endswith == ".wav":
        shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + {file_names},"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Wav_Folder\\" + {file_names})
    number + 1
    if True_files == "":
        break