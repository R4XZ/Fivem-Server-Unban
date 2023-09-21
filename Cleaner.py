import tkinter
import urllib.request
import customtkinter
import os
from PIL import Image
import shutil
import webbrowser
import pathlib

#Creates a File sto store background image in, so its not as ugly....
image_chill = ("C:\\sleepySpoofer\\")
file = pathlib.Path("C:\\sleepySpoofer\\")
if file.exists ():
    print ("File exist")
else:
    os.mkdir(image_chill)
    print("download successful")
#this is downloading the image 

pic = pathlib.Path('C:\\sleepySpoofer\\Sl33py.jpg')
if pic.exists():
    print('Picture exists')
else:
    urllib.request.urlretrieve("https://user-images.githubusercontent.com/116701630/198275317-240f0e0b-e793-4f4e-b293-4756715bb6ec.png",
    "C:\sleepySpoofer\Sl33py.jpg")
#creating the app with tkinter (icons, images, navigation etc)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SL33PY.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../test/manual_integration_tests/test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")),
                                                 dark_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")),
                                                 dark_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")),
                                                     dark_image=Image.open(os.path.join(image_path, "C:\\sleepySpoofer\\Sl33py.jpg")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  SL33PY IS LAZY", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Info",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Discord",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Rename Discord_RPC", compound="right", command=discorddll)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Cache Delete",  compound="right", command=cache)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Block Xbox",  compound="right", command=xbox)
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Spoof", compound="bottom", command=delete)
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame_button_5 = customtkinter.CTkButton(self.second_frame, text="SL33PY MADE THIS...\n\n the best free cleaner :)\n Not sure how to unban yourself?\nclick on the disocrd tab\nclick the discord button and you will be invited to the server.\n or if you wish go to my github and find the server link there.", compound="right",)
        self.second_frame_button_5.grid(row=4, column=0, padx=100, pady=150,)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame_button_6 = customtkinter.CTkButton(self.third_frame, text="Discord Invite", compound="right",command=discord_inv,)
        self.third_frame_button_6.grid(row=1, column=2, padx=200, pady=160)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Info" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Discord" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Info":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Discord":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("Info")

    def frame_3_button_event(self):
        self.select_frame_by_name("Discord")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
#deletes fivem cache
def cache():
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','data')
    shutil.rmtree(directory_path)
    directory_path2 = os.path.join(os.environ['USERPROFILE'],'AppData','Local','DigitalEntitlements')
    shutil.rmtree(directory_path2)

#Blocks Xbox 
def xbox():
    directory_path = os.path.join(os.environ['WINDIR'],'System32','drivers','etc')   
    file_path = directory_path
    file_exists = os.path.isfile(file_path)
    f = open(file_path, 'a')
    f.write('127.0.0.1 xboxlive.com\n')
    f.write('127.0.0.1 user.auth.xboxlive.com\n')
    f.write('127.0.0.1 presence-heartbeat.xboxlive.com\n')

def discorddll():    
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Roaming','discord','0.0.309','modules','discord_rpc SL33PY_SPOOFER')


def delete():
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','discord.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_chrome.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game_372.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game_1604.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game_1868.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game_2060.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX_SubProcess_game_2189.bin')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','botan.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','asi-five.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','steam.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','steam_api64.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenGame.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','profiles.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','cfx_curl_x86_64.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','CitizenFX.ini')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','caches.XML')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','adhesive.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','cfx_curl_x86_64.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','steam_api64.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','profiles.dll')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','logs')
    directory_path = os.path.join(os.environ['USERPROFILE'],'AppData','Local','FiveM','FiveM.app','crashes')

def discord_inv():
    webbrowser.open('https://discord.gg/EUBxsjdNFn')

if __name__ == "__main__":
    app = App()
    app.mainloop()

