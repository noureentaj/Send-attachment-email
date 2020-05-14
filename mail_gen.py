import configparser

from pymongo import MongoClient

from scripts import mail_module
from utils import logger
import os

cfg = configparser.RawConfigParser()
cfg.read('config.conf')
client = MongoClient(cfg.get('MONGODB', 'uri'))
zikrdb = client["ZikrDB"]
zikrcol = zikrdb["Zikr"]
path = eval(cfg.get('DUAS', 'path'))


def send_email(picture, email):
    mail_module.send_mail(picture, email)
    logger.debug("Mail sent with attachment", picture)


mail_c = zikrcol.find({})
mail_list = [each['email'] for each in mail_c]

with open("index.txt", "r+") as index:
    ind = int(index.read())
    content = os.listdir(path)
    send_email(content[ind], mail_list)
