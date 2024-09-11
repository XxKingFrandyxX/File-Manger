import os 
import sys
import shutil
import pygame

white = (255, 255, 255)
black = (0, 0, 0)

Background_color = input("Do you want a Dark or light background tpye D for dark and W for white")

if Background_color == "dark":
    Background_color = black
else:
    Background_color = white

pygame.init()
screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption("File_Manager")

screen.fill(Background_color)

pygame.display.flip()

screen = True

while screen:

    for event in pygame.event.get():

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

        print(file_names)   

        for placement in file_names:
            number = 0
            file_names[number] = placement
            True_files = str(placement)
            if True_files.endswith (".exe"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\EXE folder\\" + True_files)
                print("has been seccesfully transfered")
            if True_files.endswith (".txt"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\TXT_Folder\\" + True_files)
                print("has been seccesfully transfered")
            if True_files.endswith (".png"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Pictures Folder\\" + True_files)
                print("has been seccesfully transfered")
            if True_files.endswith (".mp4"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Videos_Folder\\" + True_files)
                print("has been seccesfully transfered")
            if True_files.endswith (".jpg"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Jpg_Folder\\" + True_files)
                print("has been seccesfully transfered")
            if True_files.endswith (".wav"):
                shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Wav_Folder\\" + True_files)
                print("has been seccesfully transfered")
            number += 1
            if placement == "":
                break

            if event.type == pygame.QUIT: 
                running = False
