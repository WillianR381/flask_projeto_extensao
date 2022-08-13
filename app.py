import os, json
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route("/",  methods=['GET'])
def home():
    with open(os.path.join(basedir, 'mockdata.json')) as f:
        data = json.load(f)
    return render_template('home.html', data=data)

@app.route("/create-client")
def create_client():
    return render_template('form-client.html' )

@app.route("/update-client/<int:id>'")
def update_client(id):
    return f'Update {id} !'

@app.route("/remove-client/<int:id>'")
def remove_client(id):
    return f'Removido {id} !'



if __name__ == "__main__":
    app.run(debug=True)