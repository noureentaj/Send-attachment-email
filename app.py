from flask import Flask, render_template, request
from pymongo import MongoClient
from configparser import RawConfigParser

app = Flask(__name__)
cfg = RawConfigParser()
cfg.read("conf/config.conf")
client = MongoClient(cfg.get('MONGODB', 'uri'))
zikrdb = client["ZikrDB"]
zikrcol = zikrdb["Zikr"]
pairing = {}


@app.route('/')
def template():
    return render_template('template.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form.get("name")
        email = request.form.get("email")
        pairing["username"] = uname
        pairing["email"] = email
        zikrcol.insert_one(pairing)
        return "Success"


if __name__ == "__main__":
    app.run(host=cfg.get('SERVICE', 'endpoint'), port=cfg.get('SERVICE', 'host'))
