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


@app.route('https://n1ckybtw.github.io/')
@app.route('https://n1ckybtw.github.io/home')
def index():
    return render_template('index.html')


@app.route("https://n1ckybtw.github.io/background")
def background():
    return render_template('background.html')


@app.route('https://n1ckybtw.github.io/final')
def final():
    return render_template('final.html')


@app.route('https://n1ckybtw.github.io/defeat')
def defeat():
    return render_template('defeat.html')


@app.route('https://n1ckybtw.github.io/1')
def first():
    return render_template('task1.html')


@app.route('https://n1ckybtw.github.io/3')
def third():
    return render_template('task3.html')


@app.route('https://n1ckybtw.github.io/4')
def forth():
    return render_template('task4.html')


@app.route('https://n1ckybtw.github.io/5')
def firth():
    return render_template('task5.html')


@app.route('https://n1ckybtw.github.io/2')
def second():
    return render_template('task2.html')


@app.route('https://n1ckybtw.github.io/tasks')
def task():
    return render_template('tasks.html')


@app.route('https://n1ckybtw.github.io/start')
def start():
    return render_template('start.html')

@app.route('https://n1ckybtw.github.io/news')
def news():
    articles = Article.query.order_by(Article.date).all()
    return render_template('news.html', articles=articles)


@app.route('https://n1ckybtw.github.io/info')
def info():
    return render_template('info.html')


@app.route('https://n1ckybtw.github.io/create', methods=['POST', 'GET'])
def create():
    if request == 'POST':
        title = request.form['title']
        intro = request.form['title']
        text = request.form['title']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('https://n1ckybtw.github.io/news')
        except:
            return 'При добавлении произошла ошибка'
    else:
        return render_template('create.html')




if __name__ == "__main__":
    app.run(debug=True)