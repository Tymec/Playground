import requests
import praw
import fire
import os
import zipfile
from PIL import Image
import ujson as json
from secrets import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT, SAVE_PATH

class ImageGrabber:
    def __init__(self, REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, 
            client_secret=REDDIT_SECRET, 
            user_agent=REDDIT_USER_AGENT)
    
    @staticmethod
    def sub_exists(sub):
        exists = True
        #try:
        #    reddit.subreddits.search_by_name(sub, exact=True)
        #except:
        #    exists = False
        return exists
    
    def getRandomSubredditPosts(self, nsfw=False, top_scale=None, limit=None):
        sub_name = self.reddit.random_subreddit(nsfw).name
        self.getSubredditImages(sub_name, top_scale, limit)
    
    def getSubredditImagesFromList(self, text_document, top_scale=None, limit=None):
        with open(text_document, 'r') as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                self.getSubredditImages(line.strip(), top_scale, limit)
        
    
    def getSubredditImages(self, sub_name, top_scale=None, limit=None):
        if not ImageGrabber.sub_exists(sub_name):
            print("Subreddit doesn't exist")
            return
        sub = self.reddit.subreddit(sub_name)
        path = SAVE_PATH + sub_name
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
        try:
            with open(save_path + ".zip", 'wb') as f:
                f.write(requests.get(url, stream=True).content)
            if zipfile.ZipFile(save_path + ".zip").testzip():
                img = Image.open(save_path + ".zip")
                img.save(save_path + ".png")
                return
            if not os.path.isdir(save_path):
                os.mkdir(save_path)
            with zipfile.ZipFile(save_path + ".zip", 'r') as zipObj:
                zipObj.extractall(save_path)
            os.remove(save_path + ".zip")
            return
        except zipfile.BadZipFile:
            return
        except KeyboardInterrupt:
            os.remove(save_path + ".zip")
            return
    
    @staticmethod
    def getVideoFile(url, save_path):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096): 
                    if chunk:
                        f.write(chunk)
                        # f.flush()
        return
        
    @staticmethod
    def getImageFile(url, save_path):
        with open(save_path, 'wb') as f:
            f.write(requests.get(url).content)
        return
    
    @staticmethod
    def getImageFromURL(url, save_path, sub_name):
        print("", end="\n")
        print("URL:" + url)
        print(f"{sub_name}: Saving...", end='\r')
        if ".com/a/" in url:
            ImageGrabber.getZipFile(url + "/zip", save_path)
            print(f"{sub_name}: Saving zip... - Success   ")
            return
        try:
            content_type = requests.head(url).headers['Content-Type'].split('/')
        except:
            print(f"{sub_name}: Saving image... - Failure")
            return
        file_extension = f".{content_type[1]}"
        if file_extension == ".*":
            return
        if content_type[0] == "image":
            ImageGrabber.getImageFile(url, save_path + file_extension)
        elif content_type[0] == "video":
            ImageGrabber.getVideoFile(url, save_path + file_extension)
        print(f"{sub_name}: Saving image... - Success ")
        return
if __name__ == "__main__":
    image_grabber = ImageGrabber(REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT)
    #image_grabber.getSubredditImages('pics', top_scale='all', limit=1000)
    #fire.Fire(image_grabber.getSubredditImages)
    fire.Fire(image_grabber.getSubredditImagesFromList)