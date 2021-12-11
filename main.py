from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@localhost:3306/python_assigment"
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Invest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount=db.Column(db.Integer,nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    garranty_id=db.Column(db.Integer,nullable=False)
    amout=db.Column(db.Integer,nullable=False)

db.create_all()
db.session.commit()

@app.route("/",methods = ["POST"])
def index():
    if request.method == "POST":
        data = request.from
        user = User(id=data.get("id"),username= data.get("userName"),email=data.get("email"))
        db.session.add(user)
        db.session.commit()

    return render_template("index.html.j2")

@app.route("/invest",methods = ["POST","GET"])
def investMoney():
    if request.method == "POST":
        data = request.from
        invest = Invest(id=data.get("id"),garranty_id=data.get("garranty_id"),amount=data.get("amount"))
        db.session.add(invest)
        db.session.commit

    return render_template("loan.html.j2")

@app.route("/pay_loan",methods = ["POST","GET"])
def investMoney():
    if request.method == "POST":
        data = request.from
        invest = Invest(id=data.get("id"),garranty_id=data.get("garranty_id"),amount=data.get("amount"))
        db.session.add(invest)
        db.session.commit

    return render_template("loan.html.j2")

if __name__ == '__main__':
    application.run(debug=True)

