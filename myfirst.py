from flask import Flask,render_template,request,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import current_app
from flask_mail import  Mail
import json
import socket
import os
from werkzeug.utils import secure_filename
print(socket.getaddrinfo('localhost', 8000))

with open('templates\config.json','r') as c:
    params=json.load(c)["PARAM"]
app = Flask(__name__)
app.secret_key='xyz-abc-pqr'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']

)
mail=Mail(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///login.db"
app.config['UPLOAD_FOLDER']=params['UPLOAD_PATH']
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    content=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self)->str:
        return f"{self.sno} - {self.title}" #to access value on print statement

class login(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.String(500),nullable=False)
    passw=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self)->str:
        return f"{self.sno} - {self.user}"

@app.route('/',methods=['GET','POST'])
def log():
    if (request.method=='POST'):
        user=request.form['username']
        passw=request.form['pass']
        print(session)
        passw2=login.query.filter_by(user=user , passw=passw).first()
        if (passw2):
            session['user']=user
            return render_template("basic.html")
        else:
            flash('Invalid credentials')
            return render_template('log.html')

    return render_template('log.html')


@app.route('/hello',methods=['GET','POST'])# method to get and receive data from website
def hello():
    if user in session:
        if request.method=='POST':
            title=request.form['title']
            content=request.form['desc']
        # f=request.files['file1']
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            todo=Todo(title=title,content=content)
            db.session.add(todo)
            db.session.commit()
            mail.send_message('new todo',sender=params['gmail-user'],recipients=[params['gmail-user']],body=title+"\n"+content)
        todolist=Todo.query.all()
        return render_template('basic.html',todolist=todolist, params=params)

@app.route("/delete/<int:sno>")
def delete(sno):
    ssno=Todo.query.filter_by(sno=sno).first()
    db.session.delete(ssno)
    db.session.commit()
    return redirect("/hello")


@app.route("/update/<int:sno>" , methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        content=request.form['desc']
        ssno=Todo.query.filter_by(sno=sno).first()
        ssno.title=title
        ssno.content=content
        db.session.add(ssno)
        db.session.commit()
        return redirect("/hello")

    ssno=Todo.query.filter_by(sno=sno).first()
    # todolist=Todo.query.all()
    return render_template('update.html',ssno=ssno)

@app.route('/uploader',methods=['GET','POST'])
def upload():
    if (request.method == 'POST'):
        f=request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return  "upload succesfully"
    else:
        return "upload unsuccesful"


@app.route('/signup',methods=['GET','POST'])
def signup():
    if (request.method=='POST'):
        user=request.form['username']
        passw=request.form['pass']
        passw2=login.query.filter_by(user=user).first()
        if(passw2):
            flash('User already exist !!! please choose another username')
            return render_template('sign.html') 
        else:
            print("entered else")
            Login=login(user=user,passw=passw)
            db.session.add(Login)
            db.session.commit()
            return redirect('/')
    return render_template('sign.html')


@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('user')
    return redirect('/')
    


if __name__=="__main__":
    # db.create_all()
    app.run(debug=True,port=8000)




