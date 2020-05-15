import configparser
from pymongo import MongoClient

cfg = configparser.RawConfigParser()
cfg.read('conf/config.conf')
uri = cfg.get('MONGODB', 'uri')
host = cfg.get('SERVICE', 'endpoint')
port = cfg.get('SERVICE', 'port')
pic_path = cfg.get('DUAS', 'path')
client = MongoClient(uri)
zikrdb = client["ZikrDB"]
zikrcol = zikrdb["Zikr"]
secure = zikrdb["securethis"]