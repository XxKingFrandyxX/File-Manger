import os 
import sys
import shutil
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

FPS = pygame.time.Clock()

Font = pygame.font.SysFont("Comic Sans MS", 24)

text = Font.render("Start", True, white)

Background_color = input("Do you want a Dark or light background tpye D for dark and W for white ")

if Background_color == "D":
    Background_color = black
    Object_Color = (128, 128, 128)
else:
    Background_color = white
    Object_Color = (128, 128, 128)


screen = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("File_Manager")

screen.fill(Background_color)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():

        FPS.tick(60)

        button_surface = pygame.Surface((150, 50))
        pygame.display.flip()

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(screen, Object_Color,(300, 500, 140, 40))
        screen.blit(text,(100,200)) 

        if event.type == pygame.MOUSEBUTTONDOWN:
               if event.type == pygame.QUIT: 
                running = False

        


       
        # Value = str("A")
        # Value = input("Hello to Fernados file manager if you want your files managed press Z ")

        # if Value == "Z":
        #     print("You have decided to continue")
        # else:  
        #     sys.exit("Thank you for not pressing Z who saved me from writing a bunch of lines")


        # list_folders = ["Pictures Folder", "Videos_Folder", "EXE folder" ,"TXT_Folder", "Jpg_Folder", "Png_Folder", "MP4_folder", "MP3_folder", "Wav_Folder", "Junk_Items"]

        # for item in list_folders:  
        #     newpath = rf"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\{item}"
        #     if not os.path.exists(newpath):
        #         os.makedirs(newpath)

        # file_names = os.listdir("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items")

        # print(file_names)   

        # for placement in file_names:
        #     number = 0
        #     file_names[number] = placement
        #     True_files = str(placement)
        #     if True_files.endswith (".exe"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\EXE folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     if True_files.endswith (".txt"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\TXT_Folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     if True_files.endswith (".png"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Pictures Folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     if True_files.endswith (".mp4"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Videos_Folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     if True_files.endswith (".jpg"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Jpg_Folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     if True_files.endswith (".wav"):
        #         shutil.move ("C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Junk_Items\\" + True_files,"C:\\Users\\Frando\\Desktop\\Work\\Programming\\File_Manger\\Wav_Folder\\" + True_files)
        #         print("has been seccesfully transfered")
        #     number += 1
        #     if placement == "":
        #         break


     


