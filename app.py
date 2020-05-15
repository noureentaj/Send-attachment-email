from flask import Flask, render_template, request
import config_handler

app = Flask(__name__)
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
        config_handler.zikrcol.insert_one(pairing)
        return "Success"


if __name__ == "__main__":
    app.run(host=config_handler.host, port=config_handler.port)
