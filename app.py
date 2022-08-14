import os, json
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "super secret key"

@app.route("/",  methods=['GET'])
def home():
    with open(os.path.join(basedir, 'mockdata.json')) as f:
        data = json.load(f)
    return render_template('home.html', data=data)


@app.route("/create-client", methods=['GET', 'POST'])
def create_client():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('form-add-client.html')


@app.route("/update-client/<int:id>", methods=['GET','POST'])
def update_client(id):
    form = {
        'first_name' : 'Willian',
        'last_name' : 'Ribeiro',
        'razao_social' : '0452424221',
        'cnpj' : '45464512',
        'email' : 'a@gmail.com',
        'phone' : '78884455',
    }

    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('form-update-client.html',id=id ,form=form )


@app.route("/remove-client/<int:id>")
def remove_client(id):
    flash("Cliente removido com Sucesso !")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)