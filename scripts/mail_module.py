import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import configparser

cfg = configparser.RawConfigParser()
cfg.read('config.conf')


def send_mail(picture, toaddr):
    msg = MIMEMultipart()
    fromaddr = "noudopy@gmail.com"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Greetings from python!"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = picture
    path = eval(cfg.get('DUAS', 'path'))
    attachment = open(path+picture, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, 'uaymhmeqmdvxaabh')
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


send_mail()
