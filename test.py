from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:20021124@127.0.0.1:5432/testdb'

db = SQLAlchemy(app)

class students(db.Model):
   __tablename__ = 'students'
   sid = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)
   tel = db.Column(db.String(50))
   address = db.Column(db.String(200))
   email = db.Column(db.String(100))

   def __init__(self, name, tel, address, email):
      self.name = name
      self.tel = tel
      self.address = address
      self.email = email

@app.route('/')
def index():
   db.create_all()

   return "DB connection success !"
# def submit():
#       if request.method == 'POST':
#         username = request.values['username']
#         password = request.values['password']
#         if username == 'admin' and password == 'admin':
#           return 'Welcome'
#         else:
#           return 'Invalid username or password'
#       return """
#         <form method="post" action = ''>
#           <p>account:<input type='text' name='username' /></p>
#           <p>password:<input type='text' name='password' /></p>
#           <p><button type='submit'> check</button></p>
#         </form>
#       """

if __name__ == '__main__':
    app.run(debug=True)