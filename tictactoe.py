from flask import Flask,render_template,request,redirect,current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///score.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)
app.app_context().push()

class TTT(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    X=db.Column(db.Integer,nullable=False,default=0)
    O=db.Column(db.Integer,nullable=False,default=0)
    TOTAL=db.Column(db.Integer,nullable=False,default=0)
    def __repr__(self)->str:
        return f"{self.Total}-{self.sno}"
# @app.route('/')
@app.route('/',methods=['GET','POST'])
def save():
    ttt=TTT( X=0,O=0,TOTAL=0)
    if request.method=='POST':
        print("POST")
        x=request.form['score_x']
        o=request.form['score_o']
        t=int(x)+int(o)
        ttt=TTT( X=x,O=o,TOTAL=t)
        db.session.add(ttt)
        db.session.commit()
    return render_template('index.html',js_files = 'static\jscript\form.js',TTT=ttt)
@app.route('/score',methods=['GET','POST'])
def score():
    
    # ttt=TTT(X,O,TOTAL)
    return render_template('score.html')


if __name__=="__main__":
    # db.create_all()
    app.run(debug=True,port=8000)

