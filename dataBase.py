import sqlite3
import pymongo
import certifi
from config.configSetup import fileRead
from config.log import get_logger

config = fileRead()

user = config["user"]
password = config["password"]
cluster = config["cluster"]
database = config["database"]

logger = get_logger(__name__)
conn = sqlite3.connect('testDB.sqlite')
cur = conn.cursor()
ca = certifi.where()
myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{cluster}.8chhr.mongodb.net/{database}?retryWrites=true&w=majority", tlsCAFile=ca)
mydb = myclient["pythonDB"]
mycol = mydb["python"]

# Checking if local table exists
def DBChecker():

    cur.execute('DROP TABLE IF EXISTS apps')

    cur.execute(
        'CREATE TABLE apps (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name TEXT, version TEXT)')
    logger.info("Local DB was dropped and a new one was created")


# Fetching data from MongoDB
def fetchDataMongo():
    data = mycol.find({})
    logger.info("Data was successfully read from MongoDB")
    return data

# Reading data from MongoDB
def readData():
    data = fetchDataMongo()
    for i in data:
        print(i)

# Adding data to local DB 
def addDataLocal(name, version):
    try:
        cur.execute(
            "INSERT INTO apps (name, version) VALUES (?, ?)", (name, version))
        conn.commit()
        logger.info("Data was successfully added to a local DB")
    except:
        logger.critical("Data was not added to local DB")

# Adding data to MongoDB
def addData(name, version):
    mydict = {"name": name, "version": version}

    try:
        x = mycol.insert_one(mydict)
        logger.info("Data was successfully added to MongoDB")
    except:
        logger.critical("Data was not added to MongoDB")
        print('Couldnt add data to MongoDB')

    try:
        cur.execute("INSERT INTO apps (name, version) VALUES (?, ?)", (name, version))
        conn.commit()
        logger.info("Data was successfully added to a local DB")

    except:
        print('Couldnt add data to local db')
        logger.critical("Data was not added to local DB")

# Adding data from MongoDB to Local DB
def MigrateData():
    try:
        data = fetchDataMongo()
        for i in data:
            addDataLocal(i.get("name"), i.get("version"))
        logger.info("Data was successfully added to local Db from MongoDB")
    except:
        print('Couldnt add data from local DB to MongoDB')
        logger.critical('Couldnt add data from local DB to MongoDB')
