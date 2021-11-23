import subprocess
import sys

# Automaticly installing all the needed packages for the programm
def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "logging"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "certifi"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymongo"])