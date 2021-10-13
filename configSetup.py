from log import *

confDict = {}
logger = get_logger(__name__)


def DefConfigSetup():
    try:
        with open('config.txt', 'x') as f:
            f.write('language: en\n')
            f.write('region: lv\n')
            f.write('supported apps:\n')
            f.write('user: guest\n')
            f.write('password: bupCsYmS3ViCwJyB\n')
            f.write('cluster: cluster0\n')
            f.write('database: pythonDB\n')
            logger.info("New config file was created")
    except:
        logger.info("Config file allready exists")


def fileRead():

    try:
        hand = open("config.txt")
        for line in hand:
            line = line.split(":")
            confDict[line[0].strip()] = line[1].strip()
        logger.info("Config file was read successfully")
        return confDict
    except:
        logger.error("Config file could not be read")
