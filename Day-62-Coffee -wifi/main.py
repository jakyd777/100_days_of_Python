from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'best secreat key'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField(label="Cafe name", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps(URL)", validators=[DataRequired(), URL()])
    time_open = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    time_close = StringField(label="Closing Time e.g. 9PM", validators=[DataRequired()])
    cafe = SelectField(label="Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi = SelectField(label="Wifi Strength", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField(label="Power Strength",choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label="Submit")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        name = form.name.data
        location = form.location.data
        time_open = form.time_open.data
        time_close = form.time_close.data
        cafe = form.cafe.data
        wifi = form.wifi.data
        power = form.power.data
        data_to_append = [name, location, time_open, time_close, cafe, wifi, power]
        with open('cafe-data.csv', "a", newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file)
            csv_data.writerow(data_to_append)
        return redirect(url_for('cafes'))
    else:
        return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
