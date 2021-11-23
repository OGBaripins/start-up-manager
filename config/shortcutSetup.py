import os
from win32com.client import Dispatch
from config.log import get_logger

logger = get_logger(__name__)

# Creating a shortcut to start the script on PC bootup
def createShortcut():
    logger.info("Script shortcut is being created")

    homedir = os.path.expanduser("~")
    path = homedir+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start.lnk"
    target = os. getcwd()+"\start.py"
    wDir = os. getcwd()
    icon = os. getcwd()+"\start.py"
    # if file exists -> return
    if(os.path.isfile(path)):
        print("Shortcut exists")
        logger.info("Script shortcut allready exists")
        return

    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()
    except Exception as e:
        logger.critical("Failed to create shortcut\n"+"err: "+e)

    logger.info("Script shortcut has been created")
    print("Shortcut created")




