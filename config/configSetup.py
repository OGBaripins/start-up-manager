from config.log import get_logger

confDict = {}
logger = get_logger(__name__)

# Method that makes default config with guest credentials for DB
def DefConfigSetup():
    try:
        with open('misc\config.txt', 'x') as f:
            f.write('[APP]\n')
            f.write('language: en\n')
            f.write('region: lv\n')
            f.write('supported apps:\n')
            
            f.write('[MONGO]:\n')
            f.write('user: guest\n')
            f.write('password: bupCsYmS3ViCwJyB\n')
            f.write('cluster: cluster0\n')
            f.write('database: pythonDB\n')
            logger.info("New config file was created")
    except:
        logger.info("Config file allready exists")

# Method that reads the config file
def fileRead():
    try:
        hand = open("misc\config.txt")
        for line in hand:
            if(line == '[APP]\n' or line == '[MONGO]\n'):
                continue
            line = line.split(":")
            confDict[line[0].strip()] = line[1].strip()
        logger.info("Config file was read successfully")
        return confDict
    except:
        logger.error("Config file could not be read")
