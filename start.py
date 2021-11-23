from config.configSetup import DefConfigSetup
from config.shortcutSetup import createShortcut
from dataBase import MigrateData

# Creating shortcuts and Def Config file
createShortcut()
DefConfigSetup()
MigrateData()
# Testing all requirments as well as running the app if tests have been passed

import config.testing
import app
