import os
import certifi
import pymongo
from configparser import ConfigParser

print("Testing all of the needed params\n\n")

# Testing if config file exists
print("Checking if config file exists:", end=' ')
try:
    assert os.path.isfile("misc\config.txt") == True
except Exception as e:
    print("Config File doesnt exist.\n")
    exit()
print("OK\n")

config = ConfigParser()
config.read('misc\config.txt')

# Testing all config file options
print("Checking [APP] options: ", end=' ')
try:
    assert config.has_option('APP', 'language') == True
    assert config.has_option('APP', 'region') == True
    assert config.has_option('APP', 'supported apps') == True
except AssertionError:
    print("App options are missing (language, region, supported apps)\n")
    exit()
print("OK\n")

print("Checking [MONGO] options: ", end=' ')
try:
    assert config.has_option('MONGO', 'user') == True
    assert config.has_option('MONGO', 'password') == True
    assert config.has_option('MONGO', 'cluster') == True
    assert config.has_option('MONGO', 'database') == True
except AssertionError:
    print("Mongo options are missing (user, password, cluster, database)\n")
    exit()
print("OK\n")

# Checking if possible to connect to MongoDb with the existing config options
print("Checking if it is possible to connect to MongoDb with the given config options:", end=' ')

ca = certifi.where()
mongodb_user = config.get('MONGO', 'user')
mongodb_password = config.get('MONGO', 'password')
mongodb_database = config.get('MONGO', 'dataBase')
mongodb_cluster = config.get('MONGO', 'cluster')

try:
    connection = pymongo.MongoClient(f"mongodb+srv://{mongodb_user}:{mongodb_password}@{mongodb_cluster}.8chhr.mongodb.net/{mongodb_database}?retryWrites=true&w=majority", tlsCAFile=ca)
    serverData = connection.admin.command('ismaster')
    assert serverData["ismaster"] == True
except:
    print("Couldn connect to MongoDB\n")
    exit()
print("OK\n")

# Testing if log file exists
print("Checking if log file exists:", end=' ')
try:
    assert os.path.isfile("misc\logs.log") == True
except:
    print("Log file doesnt exist\n")
    exit()
print("OK\n")


