from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secreat key'
API_KEY = "Your themoviedb.org API kEY "
API_TOKEN = "Your themoviedb.org API TOKEN"
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_database.db"
db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

def add_movie_to_db(movie):
    new_entry = Movie(
        title=movie["title"],
        year=movie["release_date"],
        description=movie["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
    )
    with app.app_context():
        db.session.add(new_entry)
        db.session.commit()

class AddMovieForm(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired(), Length(max=250)])
    submit = SubmitField("Add movie")
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

def find_movie(title):
    url = "https://api.themoviedb.org/3/search/movie"
    parameters = {
        "query": title,
        "include_adult": "false",
        "language": "en-US",
        "page": 1,
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(url, params=parameters, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['results']

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    num_of_films = len(all_movies)
    for i in range(0, num_of_films):
        ranking_to_change = num_of_films - i
        movie_to_update = db.get_or_404(Movie, all_movies[i].id)
        movie_to_update.ranking = ranking_to_change
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.ranking))).scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['GET', "POST"])
def edit():
    movie_id = request.args.get('id')
    form = RateMovieForm()
    # movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    movie_to_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_update, form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        all_movies = find_movie(title)
        return render_template('select.html', movies=all_movies)
    return render_template('add.html', form=form)

@app.route('/find')
def find():
    movie_id = request.args.get('id')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    movie = response.json()
    add_movie_to_db(movie)
    movie_to_change = db.session.execute(db.select(Movie).where(Movie.title == movie["title"])).scalar()
    db_movie_id = movie_to_change.id
    print(db_movie_id)
    return redirect(url_for('edit', id=db_movie_id))

if __name__ == '__main__':
    app.run(debug=True)
