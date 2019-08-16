import requests
import praw
import os
import ujson as json
from secrects.py import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT

class ImageGrabber:
    def __init__(self, REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, 
            client_secret=REDDIT_SECRET, 
            user_agent=REDDIT_USER_AGENT)

    def getRandomSubredditPosts(self, nsfw=False, top_scale=None, limit=100):
        sub_name = self.reddit.random_subreddit(nsfw).name
        self.getSubredditImages(sub_name, top_scale, limit)

    def getSubredditImages(self, sub_name, top_scale=None, limit=100):
        sub = self.reddit.subreddit(sub_name)
        
        path = f"images/{sub_name}"
        if not os.path.isdir(path):
            os.mkdir(path)
            
        if top_scale:
            sub = sub.top(top_scale)
        else:
            sub = sub.hot()
        for submission in sub:
            if submission.stickied:
                continue
            url = submission.url
            save_path = f"{path}/{submission.id}"
            image = self.getImageFromURL(url, save_path, sub_name)
        return sub

    def getBooruImage(self, url, md5, limit=20):
        params = {}
        response = requests.get(url, params=params)
        image_url = response.json()
        print(image_url)
        image = requests.get(image_url).content
        return image
    
    @staticmethod
    def getZipFile(url, save_path):
        with open(save_path, 'wb') as f:
            f.write(requests.get(url, stream=True).content)
        return
    
    @staticmethod
    def getImageFile(url, save_path):
        with open(save_path, 'wb') as f:
            f.write(requests.get(url).content)
        return
    
    @staticmethod
    def getImageFromURL(url, save_path, sub_name):
        print("", end="\n")
        print(url)
        print(f"{sub_name}: Saving image...", end='\r')
        if ".com/a/" in url:
            ImageGrabber.getZipFile(url + "/zip", save_path + ".zip")
            print(f"{sub_name}: Saving zip... - Success   ")
            return
        try:
            content_type = requests.head(url).headers['Content-Type'].split('/')
        except:
            print(f"{sub_name}: Saving image... - Failure")
            return
        if content_type[0] == "image":
            ImageGrabber.getImageFile(url, save_path + f".{content_type[1]}")
        print(f"{sub_name}: Saving image... - Success ")
        return
if __name__ == "__main__":
    image_grabber = ImageGrabber(REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT)
    image_grabber.getSubredditImages('pics', top_scale='all', limit=1000)