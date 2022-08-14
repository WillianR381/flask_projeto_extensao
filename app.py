from datetime import timedelta
import os, json
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "super secret key"

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True , autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    razao_social = db.Column(db.String(255))
    cnpj = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, first_name, last_name, razao_social, cnpj, email, phone):
        self.first_name = first_name 
        self.last_name = last_name 
        self.razao_social = razao_social 
        self.cnpj = cnpj 
        self.email = email 
        self.phone = phone 


@app.route("/",  methods=['GET'])
def home():
    data = Client.query.all()

    if not data:
        client1 = Client("Sidoney","Bimrose","Jacobs and Sons","92-7433529","sbimrose1a@wix.com","(367) 9327463")
        client2 = Client( "Elijah", "Verbrugghen","Durgan LLC", "95-3860633",  "everbrugghen1c@google.com" , "(819) 4978328")
        client3 = Client( "Rodney","Gerok","Cruickshank Group","07-8754375", "rgerok1b@icio.us","(894) 5315827")
        client4 = Client( "Cyrus","Bahls","Kunze-Casper","57-4452363","cbahls18@naver.com","(412) 7167478")
        client5 = Client("Geno","McCully","Nader Group","46-9794879","gmccully17@statcounter.com","(763) 1483610")

        db.session.add(client1)
        db.session.add(client2)
        db.session.add(client3)
        db.session.add(client4)
        db.session.add(client5)

        db.session.commit()

        data = Client.query.all()


    return render_template('home.html', data=data)


@app.route("/create-client", methods=['GET', 'POST'])
def create_client():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        razao_social = request.form.get('razao_social')
        cnpj = request.form.get('cnpj')
        email = request.form.get('email')
        phone = request.form.get('phone')

        client = Client(first_name, last_name, razao_social, cnpj, email, phone)
        
       
        
        db.session.add(client)
        db.session.commit()

        flash("Cliente cadastrado com sucesso !")
        return redirect(url_for('home'))
    else:
        return render_template('form-add-client.html')


@app.route("/update-client/<int:id>", methods=['GET','POST'])
def update_client(id):
    if request.method == 'POST':
        client = Client.query.filter_by(id=id).first_or_404()
        client.first_name = request.form.get('first_name')
        client.last_name = request.form.get('last_name')
        client.razao_social = request.form.get('razao_social')
        client.cnpj = request.form.get('cnpj')
        client.email = request.form.get('email')
        client.phone = request.form.get('phone')

        db.session.commit()

        flash(f"Cliente {client.razao_social} atualizado com sucesso !")
        return redirect(url_for('home'))
    else:
        form = Client.query.filter_by(id=id).first_or_404()
        return render_template('form-update-client.html', id=id ,form=form)


@app.route("/remove-client/<int:id>", methods=['GET'])
def remove_client(id):
    client = Client.query.filter_by(id=id).first_or_404()

    db.session.delete(client)
    db.session.commit()

    flash(f"Cliente {client.razao_social} removido com sucesso !")
    return redirect(url_for('home'))



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)