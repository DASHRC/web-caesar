from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 20px sans-serif;
                border-radius: 20px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>Rotations:
                <input name="rot" type="text" value="0"/>
            </label>
            <br>
            <textarea name="text">{0}</textarea>
            <br>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rotation = int(request.form["rot"])
    mytext = request.form["text"]
    encrypted_string = rotate_string(mytext, rotation)
    return form.format(encrypted_string)


app.run()