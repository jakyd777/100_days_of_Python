import requests

class Post:
    def __init__(self):
        api_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(api_url)
        self.all_posts = response.json()

    def get_all_posts(self):
        posts = self.all_posts
        return posts

    def get_post(self, post_num):
        for post in self.all_posts:
            if post["id"] == int(post_num):
                return post
