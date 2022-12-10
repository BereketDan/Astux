##################### import important library #################

from flask import Flask,redirect,request
from flask import render_template
from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


###################### configration app #########################

app = Flask(__name__)
app.secret_key = "onyxtechenologytrackalldevice"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
app.app_context().push()





##################### Database Model ############################

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.Integer,nullable = False ,default = 0)
    password = db.Column(db.String(200),nullable = False)
    date_add = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
    
 
 
 
 
 
 #################### Home page( index ) ########################
 
@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        user_name = request.form['name']
        user_password = request.form['password']
        new_val = User(name = user_name, password = user_password)
        
        try:
            db.session.add(new_val)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'Move on the Error'
        
    else:
       return render_template('index.html')






################### Update page ################################

@app.route('/update/')
def update():
    data_add = User.query.order_by(User.date_add).all()
    return render_template('update.html',data_add= data_add)
    




################### Remove or Delete page ########################

@app.route('/remove/<int:id>')
def delete(id):
    delete_task = User.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect(url_for('update'))
    except:
        return 'Something is off'


################## Final #######################################


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True,port = 8080)