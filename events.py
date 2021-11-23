import os.path
import webbrowser
from config.log import get_logger

logger = get_logger(__name__)

homedir = os.path.expanduser("~")

def relaxingEvent():
    logger.info("Starting 'Relaxing' event")
    try:
        webbrowser.open("https://www.youtube.com")
    except Exception as e:
        logger.critical("'Relaxing' event could not be started\n"+"Err: "+e)
        exit()
    logger.info("'Relaxing' event started successfully, exiting the programm")
    exit()

def programmingEvent():
    logger.info("Starting 'Programming' event")
    try:
        os.startfile(homedir+"\AppData\Roaming\Spotify\Spotify.exe")
        os.startfile(homedir+"\AppData\Local\Programs\Microsoft VS Code\code.exe")
    except Exception as e:
        logger.critical("'Programming' event could not be started\n"+"Err: "+e)
        exit()
    logger.info("'Programming' event started successfully, exiting the programm")
    exit()

def gamingEvent():
    logger.info("Starting 'Gaming' event")
    try:
        os.startfile(homedir+"\Desktop\Gamez")
    except Exception as e:
        logger.critical("'Gaming' event could not be started\n"+"Err: "+e)
        exit()
    logger.info("'Gaming' event started successfully, exiting the programm")
    exit()

def studyingEvent():
    logger.info("Starting 'Studying' event")
    try:
        webbrowser.open("https://www.google.com")
        webbrowser.open("https://lekcijas.va.lv/")
        webbrowser.open("https://moodle.va.lv/")
        webbrowser.open("https://outlook.office.com/owa/")
    except Exception as e:
        logger.critical("'Studying' event could not be started\n"+"Err: "+e)
        exit()
    logger.info("'Studying' event started successfully, exiting the programm")
    exit()

def workoutEvent():
    logger.info("Starting 'Workout' event")
    try:
        os.startfile(homedir+"\AppData\Roaming\Spotify\Spotify.exe")
    except Exception as e:
        logger.critical("'Workout' event could not be started\n"+"Err: "+e)
        exit()
    logger.info("'Workout' event started successfully, exiting the programm")
    exit()
