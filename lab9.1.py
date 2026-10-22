#Вариант 1
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    important = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Note{self.id}.{self.text}'


@app.route('/')
def main():
    notes = Note.query.all()
    return render_template('index.html', notes_list=notes)


@app.route('/add', methods = ['POST'])
def add_note():
    data = request.json
    note = Note(**data)
    db.session.add(note)
    db.session.commit()
    return ('OK')


@app.route('/clear', methods = ['DELETE'])
def clear_notes():
   Note.query.delete()
   db.session.commit()
   return ('OK')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

