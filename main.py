from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json

with open('config.json','r') as c:
    params= json.load(c)['params']
local_server=True


app = Flask(__name__)  #Creating object of flask

#Automated Mail
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)

mail = Mail(app)

#configuiring MySQL URI  for SQLAlchemy Database
#URI can be obtained by googling 
#username is root for standard installation of xamapp and password is to be deleted and kept blank
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)        

#Inherited Class comprising of colunms to  database is made
#refer https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/?highlight=quick%20start for more details

class Contact(db.Model):
    '''sno, name, email, phone_num, mes, date'''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone_num = db.Column(db.String(13), unique=True, nullable=False)
    msg = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.String(12), unique=True, nullable=True)

class Posts(db.Model):
    '''sno, name, email, phone_num, mes, date'''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)
    subtitle = db.Column(db.String(30), unique=False, nullable=True)
    content = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(20), unique=False, nullable=False)
    img_file = db.Column(db.String(30), unique=True, nullable=True)
    date = db.Column(db.String(12), unique=True, nullable=True)

@app.route("/")
def home():
    posts= Posts.query.filter_by().all()
    return render_template("index.html", params=params, posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", params=params)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method=='POST'):
        '''Add entry to data base'''
        name= request.form.get("name")
        email= request.form.get("email")
        phone= request.form.get("phone")
        message = request.form.get("message")

        '''sno, name, email, phone_num, mes, date'''
        entry = Contact(name=name, phone_num =phone , email= email, msg = message, date = datetime.now())
        mail.send_message(
            "New message from blog", 
            sender=email, 
            recipients= [params['gmail-user']],
            body= f"New Message from {name}.\n{message}\nSender phone: {phone}",
        )
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html", params=params)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):
    post= Posts.query.filter_by(slug=post_slug).first()
    
    return render_template("post.html", params=params, post=post)

app.run(debug=True)
