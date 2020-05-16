import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config_handler


def send_mail(picture, toaddr):
    msg = MIMEMultipart()

    fromaddr = "noudopy@gmail.com"
    msg['From'] = "NoudoPy"
    msg['Subject'] = "Read Dua attached, right now"

    with open("templates/email_temp.html", "r+") as html_file:
        html = html_file.read()
    filepath = f'"http://159.89.175.76/duas/{picture}"'
    html = html.replace("$$IMAGE$$", filepath)

    msg.attach(MIMEText(html, 'html'))

    # msg.attach(MIMEText(body, 'plain'))
    # filename = picture
    # path = eval(config_handler.pic_path)
    # attachment = open(path + filename, "rb")

    # p = MIMEBase('application', 'octet-stream')
    # p.set_payload(attachment.read())
    # encoders.encode_base64(p)
    # p.add_header('Content-Disposition', f"attachment; filename= {filename}")
    # msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, config_handler.password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)
    s.quit()
