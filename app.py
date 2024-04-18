from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intro = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(500), default=datetime.now)

    def __repr__(self):
        return  '<Article %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/background")
def background():
    return render_template('background.html')


@app.route('/final')
def final():
    return render_template('final.html')


@app.route('/defeat')
def defeat():
    return render_template('defeat.html')


@app.route('/1')
def first():
    return render_template('task1.html')


@app.route('/3')
def third():
    return render_template('task3.html')


@app.route('/4')
def forth():
    return render_template('task4.html')


@app.route('/5')
def firth():
    return render_template('task5.html')


@app.route('/2')
def second():
    return render_template('task2.html')


@app.route('/tasks')
def task():
    return render_template('task.html')


@app.route('/start')
def start():
    return render_template('startgame.html')

@app.route('/news')
def news():
    articles = Article.query.order_by(Article.date).all()
    return render_template('news.html', articles=articles)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request == 'POST':
        title = request.form['title']
        intro = request.form['title']
        text = request.form['title']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/news')
        except:
            return 'При добавлении произошла ошибка'
    else:
        return render_template('create.html')




if __name__ == "__main__":
    app.run(debug=True)