from flask import Flask, render_template
import post
from post import Post

all_post = Post()

app = Flask(__name__)

@app.route('/')
def home():
    posts = all_post.get_all_posts()
    return render_template("index.html", posts=posts)

@app.route('/post/<number>')
def get_post(number):
    choose_post = all_post.get_post(number)
    return render_template("post.html", post=choose_post)

if __name__ == "__main__":
    app.run(debug=True)
