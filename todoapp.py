from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoapp.db'
db= SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200))
  completed = db.Column(db.Boolean)


@app.route("/")
def index():
  cards = Todo.query.filter_by(completed=False).all()
  crushed= Todo.query.filter_by(completed=True).all()
  alldb = Todo.query.all()

  return(render_template('layout.html', cards = cards, crushed= crushed, all = alldb))

@app.route("/add", methods=["POST"])
def add():
  todo =Todo(text = request.form.get("card"), completed=False)
  db.session.add(todo)
  db.session.commit()
  return (redirect(url_for('index')))

@app.route("/complete/<id>")
def complete(id):
  todo = Todo.query.filter_by(id=int(id)).first()
  todo.completed = True
  db.session.commit()
  return redirect(url_for('index'))

@app.route("/delete/<id>")
def delete(id):
  todo = Todo.query.filter_by(id=int(id)).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ =='__main__':
  app.run(debug=True)
