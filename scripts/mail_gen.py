from utils import logger
from scripts import mail_module
import time
import os
import configparser
from pymongo import MongoClient

cfg = configparser.RawConfigParser()
cfg.read('config.conf')
client = MongoClient(cfg.get('MONGODB', 'uri'))
zikrdb = client["ZikrDB"]
zikrcol = zikrdb["Zikr"]
path = eval(cfg.get('DUAS', 'path'))


def send_email(picture,email):
    mail_module.send_mail(picture, email)
    logger.debug("Mail sent with attachment", picture)
    time.sleep(60 * 60 * 24)


mail_c = zikrcol.find({})
mail_list = [each['email'] for each in mail_c]

for each_picture in os.listdir(path):
    for each_mail in mail_list:
        send_email(each_picture, each_mail)
