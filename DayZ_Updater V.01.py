import pygame,sys,os,shutil
from button import button
from distutils.dir_util import copy_tree
import subprocess as sp
from tkinter import *
from tkinter import filedialog
from pymem import Pymem
from pgu import gui

batch_dir = ''
server_dir = ''

#set bat file to launch server  
def set_bat():
    try:
        #retrieve current user path *C:\Users\Zippe*
        user_path = os.path.expanduser('~')
        bdir = []

        def openFile():
            filepath = filedialog.askdirectory(initialdir=user_path)
            server_dir = filepath
            server_dir.replace("/","\\")
            bdir.append(server_dir)

        window = Tk()
        button = Button(text="Open",command=openFile)
        button.pack()
        window.mainloop()
        batch_dir = str(bdir[0])
        return batch_dir
    except:
        print('error')
        return "None"
            
#ret set bat name
def ret_bat():
    try:
        lis = os.listdir(server_dir)
        for l in lis:
            if".bat"in l:
                batch_dir = server_dir+"\\"+l
                print(batch_dir)
                return batch_dir
    except:
        print('error')
        return "None"
    
#ret path manually
def ret_path():
    try:
        lis = os.listdir("C:\Program Files (x86)\Steam\steamapps\common")
        for l in lis:
            if"DayZServer"in l:
                server_dir = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\"+l
                print(server_dir)
                return server_dir
    except:
        print('error')
        return "None"

#set path
def set_path():
    server_dir = ''
    try:
        #retrieve current user path *C:\Users\Zippe*
        user_path = os.path.expanduser('~')
        sdir = []

        def openFile():
            filepath = filedialog.askdirectory(initialdir=user_path)
            server_dir = filepath
            server_dir.replace("/","\\")
            sdir.append(server_dir)

        window = Tk()
        button = Button(text="Open",command=openFile)
        button.pack()
        window.mainloop()
        server_dir = str(sdir[0])
        return str(server_dir)
    except:
        print('error')
        return str("None")

class Controller:
    def __init__(self,server_dir,batch_dir):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        size = w,h = 800,800
        header_w,header_h = 450,175
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("DayZ Server Controller v.01")

        #header, background, logo, & icon
        self.icon = pygame.image.load("Assets\main\logo_transparent.png").convert_alpha()
        self.header_bkgrd = pygame.image.load("Assets\main\header.png").convert_alpha()
        self.header_bkgrd = pygame.transform.scale(self.header_bkgrd,(header_w,header_h))
        self.header_title = pygame.image.load("Assets\main\header_title_tran.png").convert_alpha()
        self.header_title = pygame.transform.scale(self.header_title,(header_w,header_h))
        self.bkgrd_img = pygame.image.load("Assets\\main\\bckgrd.jfif").convert_alpha()
        self.bkgrd_img = pygame.transform.scale(self.bkgrd_img,(w,h-header_h))

        #button images main menu
        self.srv_upd_btn = pygame.image.load("Assets\\buttons\\button (11).png").convert_alpha()
        self.srv_upd_btn_hgh = pygame.image.load("Assets\\buttons\\button (1).png").convert_alpha()
        self.srv_path_btn = pygame.image.load("Assets\\buttons\\button (12).png").convert_alpha()
        self.srv_path_btn_hgh = pygame.image.load("Assets\\buttons\\button (4).png").convert_alpha()
        self.add_mods_btn = pygame.image.load("Assets\\buttons\\button (9).png").convert_alpha()
        self.add_mods_btn_hgh = pygame.image.load("Assets\\buttons\\button (2).png").convert_alpha()
        self.rmv_mods_btn = pygame.image.load("Assets\\buttons\\button (10).png").convert_alpha()
        self.rmv_mods_btn_hgh = pygame.image.load("Assets\\buttons\\button (3).png").convert_alpha()
        self.all_mods_btn = pygame.image.load("Assets\\buttons\\button (7).png").convert_alpha()
        self.all_mods_btn_hgh = pygame.image.load("Assets\\buttons\\button (6).png").convert_alpha()
        self.rst_cach_btn = pygame.image.load("Assets\\buttons\\button (8).png").convert_alpha()
        self.rst_cach_btn_hgh = pygame.image.load("Assets\\buttons\\button (5).png").convert_alpha()
        self.lnc_srv_btn = pygame.image.load("Assets\\buttons\\button (13).png").convert_alpha()
        self.lnc_srv_btn_hgh = pygame.image.load("Assets\\buttons\\button (14).png").convert_alpha()
        self.sht_srv_btn = pygame.image.load("Assets\\buttons\\button (16).png").convert_alpha()
        self.sht_srv_btn_hgh = pygame.image.load("Assets\\buttons\\button (15).png").convert_alpha()

        #button images source path

        #init buttons main menu
        self.update_btn = button(100,275,self.srv_upd_btn,1.0)
        self.server_path_btn = button(500,275,self.srv_path_btn,1.0)
        self.add_mod_btn = button(100,400,self.add_mods_btn,1.0)
        self.remove_mod_btn = button(500,400,self.rmv_mods_btn,1.0)
        self.load_all_btn = button(100,525,self.all_mods_btn,1.0)
        self.reset_cache_btn = button(500,525,self.rst_cach_btn,1.0)
        self.start_server = button(100,650,self.lnc_srv_btn,1.0)
        self.shut_server = button(500,650,self.sht_srv_btn,1.0)

        #init buttons source path

        #set icon & init clock
        pygame.display.set_icon(self.icon)

        self.chime = "Assets\\notifications\\succ (1).wav"
        self.tone = "Assets\\notifications\\click err.wav"
        self.on = "Assets\\notifications\\on.wav"
        BLACK = 0,0,0
        self.BCKGD = 78,15,114
        m = pygame.mixer

        self.main_surface = pygame.Surface((w,h-header_h),masks=(BLACK))
        self.screen = screen
        self.main = False
        self.kill = "DayZServer_x64.exe"
        self.server_dir = server_dir
        self.batch_dir = batch_dir
        self.input = []
        self.clock = pygame.time.Clock()
        self.FPS = 60
        # with open("my_file.txt", "a") as f:
        
    def succ_not(self):
        succ1 = pygame.mixer.music.load(self.chime)
        pygame.mixer.music.play()
            
        
    def err_not(self):
        succ2 = pygame.mixer.music.load(self.tone)
        pygame.mixer.music.play()
        
    def on_not(self):
        succ3 = pygame.mixer.music.load(self.on)
        pygame.mixer.music.play()
      
    #update menu
    def update(self,path):
        try:
            mods = os.listdir(path)
            mods_up = []
            for mod in mods:
                if "@" in mod:
                    mods_up.append(mod)
                else:
                    continue
            for mod in mods_up:
                from_dir = r"C:\Program Files (x86)\Steam\steamapps\common\DayZ\!Workshop"+"\\"+mod
                to_dir = path+"\\"+mod
        
                copy_tree(from_dir, to_dir)
                print(f'[{mod} Succesfully Loaded]')
                key_from_directory = path+"\\"+mod+r"\Keys"
                key_to_directory = path+"\keys"
                key_to_directory = str(key_to_directory)
                copy_tree(key_from_directory,key_to_directory)
                print(f"[key for mod {mod} succesfully completed]\n")
            print(f'\n\n[Server Mods Loaded]\n\n')
            self.succ_not()
            return True
        except:
            self.err_not()
            return False
    
    #server path
    def server_path(self):
            if len(self.server_dir) >1:
                return True
            else:
                return False
    
    #add selected mods
    def add_mods(self):
        self.main=False
        try:          
            sys.path.insert(0, '..')
            dirs = []

            def open_file_browser(arg):
                d = gui.FileDialog()
                d.connect(gui.CHANGE, handle_file_browser_closed, d)
                d.open()
                
            def handle_file_browser_closed(dlg):
                if dlg.value: input_file.value = dlg.value
                dirs.append(dlg.value)
                print(dirs)

            #gui.theme.load('../data/themes/default')
            app = gui.Desktop()
            app.connect(gui.QUIT,app.quit,None)
            main = gui.Container(width=500, height=400) #, background=(220, 220, 220) )

            #add Title label with html tag h1
            main.add(gui.Label("FileDialog System", cls="h1"), 500//4, 20)
            main.add(gui.Label("Adding mods to your Server", cls="h2"), 500//4, 150)
            main.add(gui.Label("Select the 'Browse..' button", cls="h5"), 500//4, 190)
            main.add(gui.Label("Locate desired mod & click 'Okay'", cls="h5"), 500//4, 210)
            main.add(gui.Label("When you are ready close FileDialog", cls="h5"), 500//4, 230)

            td_style = {'padding_left': 10}
            t = gui.Table()
            t.tr()
            t.td( gui.Label('File Name:') , style=td_style )
            input_file = gui.Input()
            t.td( input_file, style=td_style )
            b = gui.Button("Browse...")
            t.td( b, style=td_style )
            b.connect(gui.CLICK, open_file_browser, None)

            #add text input for user
            main.add(t, 20, 100)
            
            app.run(main)
            #import profile
            #profile.run('app.run(main)')
            
            #Try removing server path from second filedialog
            
            for mod in dirs:
                if"@"in mod:
                    mod = str(mod)
                    modw = mod.replace("C:\Program Files (x86)\Steam\steamapps\common\DayZ\!Workshop\\","")
                    print(modw)
                    from_dir = r"C:\Program Files (x86)\Steam\steamapps\common\DayZ\!Workshop"+"\\"+modw
                    to_dir = self.server_dir+"\\"+modw
            
                    copy_tree(from_dir, to_dir)
                    print(f'[{modw} Succesfully Loaded]')
                    key_from_directory = self.server_dir+"\\"+modw+r"\Keys"
                    key_to_directory = self.server_dir+"\keys"
                    key_to_directory = str(key_to_directory)
                    copy_tree(key_from_directory,key_to_directory)
                    print(f"[key for mod {modw} succesfully completed]\n")
                print(f'\n\n[Server Mods Loaded]\n\n')
            self.main = True
            return True
        except:
            self.main = True
            return False
    
    #remove selected mods
    def rem_mods(self):
        self.main = False
        try:          
            sys.path.insert(0, '..')
            dirs = []

            def open_file_browser(arg):
                d = gui.FileDialog()
                d.connect(gui.CHANGE, handle_file_browser_closed, d)
                d.open()
                
            def handle_file_browser_closed(dlg):
                if dlg.value: input_file.value = dlg.value
                dirs.append(dlg.value)
                print(dirs)

            #gui.theme.load('../data/themes/default')
            app = gui.Desktop()
            app.connect(gui.QUIT,app.quit,None)
            main = gui.Container(width=500, height=400) #, background=(220, 220, 220) )

            #add Title label with html tag h1
            main.add(gui.Label("FileDialog System", cls="h1"), 500//4, 20)
            main.add(gui.Label("Removing mods from server", cls="h2"), 500//4, 150)
            main.add(gui.Label("Select the 'Browse..' button", cls="h5"), 500//4, 190)
            main.add(gui.Label("Locate desired mod & click 'Okay'", cls="h5"), 500//4, 210)
            main.add(gui.Label("When you are ready close FileDialog", cls="h5"), 500//4, 230)

            td_style = {'padding_left': 10}
            t = gui.Table()
            t.tr()
            t.td( gui.Label('File Name:') , style=td_style )
            input_file = gui.Input()
            t.td( input_file, style=td_style )
            b = gui.Button("Browse...")
            t.td( b, style=td_style )
            b.connect(gui.CLICK, open_file_browser, None)

            #add text input for user
            main.add(t, 20, 100)
            
            app.run(main)
            #import profile
            #profile.run('app.run(main)')
            
            #Try removing server path from second filedialog
            
            for mod in dirs:
                if"@"in mod:
                    server_dir = str(self.server_dir)
                    mod = str(mod)
                    modw = mod.replace(server_dir,"")
                    modw = modw.replace("\\","")
                    print(modw)
                    from_dir = server_dir+"\\"+modw
                    key_dir = server_dir+"\\"+r"Keys"
                    
            
                    #remove mod from serverdir if mod
                    try:
                        shutil.rmtree(from_dir)
                        shutil.rmtree(key_dir)
                        print("Removed")
                        self.main = True
                        return True
                    except:
                        print("Exception")
                        self.main = True
            self.main = True
        except:
            print("Mod failed to remove")
            self.main = True
            return False
    
    #load all mods
    def add_all_mods(self,path):
        try:
            mods = os.listdir(r"C:\Program Files (x86)\Steam\steamapps\common\DayZ\!Workshop")
            for mod in mods:
                from_dir = r"C:\Program Files (x86)\Steam\steamapps\common\DayZ\!Workshop"+"\\"+mod
                to_dir = path+"\\"+mod
        
                copy_tree(from_dir, to_dir)
                print(f'[{mod} Succesfully Loaded]')
                key_from_directory = path+"\\"+mod+r"\Keys"
                key_to_directory = path+"\keys"
                key_to_directory = str(key_to_directory)
                copy_tree(key_from_directory,key_to_directory)
                print(f"[key for mod {mod} succesfully completed]\n")
            print(f'\n\n[Server Mods Loaded]\n\n')
            return True
        except:
            print(f'[{Exception}]')
            print(f'\n\n[Server Mods In-complete]\n\n')
            return False
        
    #reset cache
    def reset(self):
        try:
            cache_path = r"\mpmissions\dayzOffline.chernarusplus\storage_1"
            path = self.server_dir+cache_path
            shutil.rmtree(path)
            print("Cache Data Reset")
            return True
        except:
            print("Verify your server path is correct")
            return False
    
    #launch server('s)
    def launch(self):
        try:
            #cut key for launch
            print("launching server")
            sp.Popen(self.batch_dir)
            return True
        except:
            return False
    
    #shutdown server('s)
    def shutdown(self):
        try:
            os.system("taskkill /f /im "+self.kill)
            return True
        except:
            print("Error in striking")
            return False
        
    def check_if_running(self,pid):
        try:
            pm = Pymem(pid)
            return True

        except:
            return False
    
    #main menu
    def run(self):
        self.main = True
        while self.main:
            self.clock.tick(self.FPS)
            #add pyagme quit method
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            #load logo & scale size
            logo = pygame.image.load("Assets\main\logo_.png").convert_alpha()
            logo = pygame.transform.scale(logo,(175,175))  
                    
            #set bg color & header
            self.screen.fill(self.BCKGD)
            self.screen.blit(self.header_bkgrd,(175,0))
            self.screen.blit(self.header_title,(175,0))
            self.screen.blit(self.main_surface,(0,175))
            self.main_surface.blit(self.bkgrd_img,(0,0))
            
            #add buttons
            if self.update_btn.draw(self.srv_upd_btn,self.srv_upd_btn_hgh,self.screen):
                if self.update(self.server_dir):
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.server_path_btn.draw(self.srv_path_btn,self.srv_path_btn_hgh,self.screen):
                if self.server_path():
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.add_mod_btn.draw(self.add_mods_btn,self.add_mods_btn_hgh,self.screen):
                #CURRENTLY NOT WORKING. TK and PYGAME Xx Crash eachother xX              
                if self.add_mods():
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.remove_mod_btn.draw(self.rmv_mods_btn,self.rmv_mods_btn_hgh,self.screen):
                #CURRENTLY NOT WORKING. TK and PYGAME Xx Crash eachother xX
                #maybe add subscreen for option [1.remove selected 2.remove all]
                if self.rem_mods():
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.load_all_btn.draw(self.all_mods_btn,self.all_mods_btn_hgh,self.screen):
                if self.add_all_mods(self.server_dir):
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.reset_cache_btn.draw(self.rst_cach_btn,self.rst_cach_btn_hgh,self.screen):
                if self.reset():
                    self.succ_not()
                else:
                    self.err_not()
                
            if self.start_server.draw(self.lnc_srv_btn,self.lnc_srv_btn_hgh,self.screen):
                if self.launch():
                    self.succ_not()
                else:
                    self.err_not()
                    
            if self.shut_server.draw(self.sht_srv_btn,self.sht_srv_btn_hgh,self.screen):
                if self.check_if_running(self.kill):
                    if self.shutdown()==True:
                        self.succ_not()
                else:
                    self.err_not()
            
            #add logo to header
            self.screen.blit(logo,(0,0))
            self.screen.blit(logo,(800-175,0))
            
            #update display
            pygame.display.flip()

if __name__=="__main__":
    #attempt retrieval of serverpath
    vr = ret_path()
    vr = str(vr)
    if "None"not in vr:
        server_dir = vr
        vr = ret_bat()
        if "None"not in vr:
            batch_dir = vr
            main = Controller(server_dir,batch_dir)
            main.on_not()
            main.run()
        elif "None"in vr:
            vr = set_bat()
            if "None"not in vr:
                batch_dir = vr
                main = Controller(server_dir,batch_dir)
                main.run()
                main.on_not()
            elif "None"in vr:
                print("error in set bat")
    elif "None"in vr:
        vr = set_path()
        if "None"not in vr:
            server_dir = vr
            vr = ret_bat()
            if "None"not in vr:
                batch_dir = vr
                main = Controller(server_dir,batch_dir)
                main.run()
                main.on_not()
            elif "None"in vr:
                vr = set_bat()
                if "None"not in vr:
                    batch_dir = vr
                    main = Controller(server_dir,batch_dir)
                    main.run()
                    main.on_not()
                elif "None"in vr:
                    print("error in set bat")
        elif "None"in vr:
            print("error in set path")