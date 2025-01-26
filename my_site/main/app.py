from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['WTF_CSRF_ENABLED'] = False

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        new_message = Message(username=username, message=message)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('index'))

    messages = Message.query.all()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    db.create_all()  # Создание базы данных
    app.run(debug=True)