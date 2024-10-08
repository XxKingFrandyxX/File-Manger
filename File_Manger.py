import os 
import sys
import shutil
import wx
from tqdm.auto import tqdm 


      #Template   
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title="File Manager")
        panel = wx.Panel(self)
        button_sizer = wx.BoxSizer(wx.VERTICAL) 

        Button_play = wx.Button(panel, label = "Start")
        button_quit = wx.Button(panel, label = "Quit Program") 
        button_sizer.Add(Button_play,  0, wx.ALL | wx.CENTER, 5)
        button_sizer.Add(button_quit, 0, wx.ALL | wx.CENTER, 5)

        button_quit.Bind(wx.EVT_BUTTON, self.quit)
        Button_play.Bind(wx.EVT_BUTTON, self.start)

        panel.SetSizer(button_sizer)  
        self.Show()

    def quit (self, event):
        sys.exit("See Ya Later!!")

    
    def start (self, event):

        for Progressbar in tqdm(range(10000)):
            print(" ", end='\r')


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

        

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

    # import pygame

# pygame.init()

# white = (255, 255, 255)
# black = (0, 0, 0)

# FPS = pygame.time.Clock()

# Font = pygame.font.SysFont("Comic Sans MS", 24)

# text = Font.render("Start", True, white)

# Background_color = input("Do you want a Dark or light background tpye D for dark and W for white ")

# if Background_color == "D":
#     Background_color = black
#     Object_Color = (128, 128, 128)
# else:
#     Background_color = white
#     Object_Color = (128, 128, 128)


# screen = pygame.display.set_mode((1920, 1080))

# pygame.display.set_caption("File_Manager")

# screen.fill(Background_color)

# pygame.display.flip()

# running = True

# while running:

#     for event in pygame.event.get():

#         FPS.tick(60)

#         button_surface = pygame.Surface((150, 50))
#         pygame.display.flip()

#         mouse = pygame.mouse.get_pos()

#         pygame.draw.rect(screen, Object_Color,(300, 500, 140, 40))
#         screen.blit(text,(100,200)) 

#         if event.type == pygame.MOUSEBUTTONDOWN:
#                if event.type == pygame.QUIT: 
#                 running = False






