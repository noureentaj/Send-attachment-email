import os
import config_handler
from scripts import mail_module_html
from utils.logger import logger

path = eval(config_handler.pic_path)


def send_email(email):
    mail_module_html.send_mail(email)
    # logger.debug("Mail sent with attachment", picture)


mail_c = config_handler.zikrcol.find({})
mail_list = [each['email'] for each in mail_c]

with open("index.txt", "r+") as index:
    ind = int(index.read())
index.close()

content = os.listdir(path)

send_email(mail_list)
print("Send dua number",ind)
ind = ind + 1
with open("index.txt", "w+") as rew:
    rew.write(str(ind))
rew.close()

