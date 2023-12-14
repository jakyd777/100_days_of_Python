from flask import Flask
import random


rand_number = random.randint(0, 9)
print(rand_number)

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1>Guess a number between 0 and 9</1>' \
            '<div><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></div>'

@app.route('/<int:number>')
def check_number(number):

    if number > rand_number:
        return '<h1 style="color:blue">Too high, try again!</1>' \
                '<div><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></div>'
    elif number < rand_number:
        return '<h1 style="color:red">Too low, try again!</1>' \
                '<div><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></div>'
    else:
        return '<h1 style="color:green">You found me!</1>' \
                '<div><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></div>'

if __name__ == '__main__':
    app.run(debug=True)


