import requests
import praw
import fire
import os
import zipfile
import time
import atexit
import uuid
import twitter
import youtube_dl
from PIL import Image
import ujson as json
from gfycat.client import GfycatClient
from gfycat.error import GfycatClientError
from secrets import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT, GFYCAT_CLIENT_ID, GFYCAT_SECRET, TWITTER_API_KEY, TWITTER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, SAVE_PATH

LOG_VERBOSE = False

class ImageGrabber:
    GRAB_DELAY = 0 # Needs fixing
    ENDER_FILE = SAVE_PATH + ".ender"

    def __init__(self, REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT):
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, 
            client_secret=REDDIT_SECRET, 
            user_agent=REDDIT_USER_AGENT)
        self.gfycat = GfycatClient(GFYCAT_CLIENT_ID, GFYCAT_SECRET)
        self.twitter = twitter.Api(consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_SECRET, access_token_key=TWITTER_ACCESS_KEY, access_token_secret=TWITTER_ACCESS_SECRET)
        
        
        open('ImageGrabber.log', 'w').close()
        self.logToFile("Initializing...", 0, _print=False)
        self.progress = self.loadProgress()
        self.API_USAGE_MAP = {
            "gfycat": self.downloadGfycat,
            "imgur": self.downloadImgur,
            "redd.it": self.downloadReddit,
            "reddituploads": self.downloadReddit,
            "tumblr": self.downloadTumblr,
            "twitter": self.downloadTwitter,
            
            "=_*-default-*_=": self.downloadYoutube,
            "reddit,comments": self.ignoreDownload
        }
    
    @staticmethod
    def sub_exists(sub):
        exists = True
        #try:
        #    reddit.subreddits.search_by_name(sub, exact=True)
        #except:
        #    exists = False
        return exists
    
    def loadProgress(self):
        progress = {}
        
        if not os.path.exists(self.ENDER_FILE):
            open(self.ENDER_FILE, 'a').close()
            print("Save file not found, creating a new one...")
            return progress
        
        with open(self.ENDER_FILE, 'r') as f:
            try:
                progress = json.load(f)
            except ValueError:
                progress = {}
        
        if progress == {}:
            print("Save file empty or corrupt, resetting...")
        
        return progress
    
    def save(self):
        with open(self.ENDER_FILE, 'w') as f:
            json.dump(self.progress, f)
    
    def saveProgress(self, sub_name, top_scale, limit):
        with open(self.ENDER_FILE, 'w') as f:
            self.progress[sub_name] = {
                "top_scale": top_scale,
                "limit": limit,
                "time": time.time()
            }
            json.dump(self.progress, f)
    
    def getRandomSubredditPosts(self, nsfw=False, top_scale=None, limit=None):
        sub_name = self.reddit.random_subreddit(nsfw).name
        self.getSubredditImages(sub_name, top_scale, limit)
    
    def getMediaFromList(self, text_document):
        path = 'links//'
        if not os.path.isdir(path):
            os.mkdir(path)
    
        with open(text_document, 'r') as f:
            for line in f.readlines():
                if line.startswith('#') or line == "":
                    continue
                print(f"{line.strip()}: Processing...")
                self.getMediaFromURL(line.strip(), path + uuid.uuid4().hex) 
    
    def getSubredditImagesFromList(self, text_document, top_scale=None, limit=None):
        with open(text_document, 'r') as f:
            for line in f.readlines():
                if line.startswith('#') or line == "":
                    continue
                print(f"{line.strip()}: Processing...")
                self.getSubredditImages(line.strip(), top_scale, limit)    
    
    def getSubredditImages(self, sub_name, top_scale=None, limit=None):
        if not ImageGrabber.sub_exists(sub_name):
            print("Subreddit doesn't exist")
            return
        
        sub = self.reddit.subreddit(sub_name)
        path = SAVE_PATH + sub_name
        
        if sub_name in self.progress:
            _top = top_scale if top_scale != None else "hot"
            _sub = self.progress[sub_name]
            if _sub['top_scale'] == _top and _sub['limit'] == limit:
                if (time.time() - _sub['time']) < self.GRAB_DELAY:
                    if os.path.isdir(path):
                        print("Already grabbed this sub, skipping...")
                        return
        
        if not os.path.isdir(path):
            os.mkdir(path)
        
        if not limit:
            limit = 100
        
        if top_scale:
            sub = sub.top(top_scale, limit=limit)
        else:
            sub = sub.hot(limit=limit)
        for submission in sub:
            if submission.stickied:
                continue
            url = submission.url
            save_path = f"{path}/{submission.id}"
            image = self.getMediaFromURL(url, save_path)
            
        self.saveProgress(sub_name, top_scale, limit)
        return sub
    
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
    def getVideoFile(url, save_path, stream=True, chunk_size=4096):
        with requests.get(url, stream=stream) as r:
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size): 
                    if chunk:
                        f.write(chunk)
                        # f.flush()
        return
        
    @staticmethod
    def getImageFile(url, save_path):
        with open(save_path, 'wb') as f:
            f.write(requests.get(url).content)
        return
    
    def logResponse(self, error_code):
        if error_code == 1:
            self.logToFile("General: Successfully saved image file", error_code)
        elif error_code == 2:
            self.logToFile("Tumblr: Successfully saved '.zip' file", error_code)
        elif error_code == 3:
            self.logToFile("General: Successfully saved video file", error_code)
        elif error_code == 4:
            self.logToFile("Youtube-dl: Successfully saved media", error_code)   
            
        elif error_code == -1:
            self.logToFile("General: Failed to save image", error_code)
        elif error_code == -2:
            self.logToFile("General: File extension '.*' not supported", error_code)
        elif error_code == -3:
            self.logToFile("Gfycat: Video no longer exists", error_code)
        elif error_code == -4:
            self.logToFile("Twitter: No video was found", error_code)
        elif error_code == -5:
            self.logToFile("Internal: API for URL is not implemented yet", error_code)
        elif error_code == -6:
            self.logToFile("General: Failed to fetch content type", error_code)
        elif error_code == -7:
            self.logToFile("General: Skipping ignored URL", error_code)
        elif error_code == -8:
            self.logToFile("Youtube-dl: Failed to fetch media", error_code)
        else:
            self.logToFile("Internal: Error code unknown", error_code)
    
    @staticmethod
    def logToFile(error, code, _print=True):
        if LOG_VERBOSE and _print:
            print(error)
        
        with open('ImageGrabber.log', 'a') as f:
            f.write(error)
    
    def getMediaFromURL(self, url, save_path):
        if LOG_VERBOSE:
            self.logToFile(f"URL: {url}", 0, _print=False)
        
        current_api = None
        for api in self.API_USAGE_MAP.keys():
            if any(_api in url for _api in api.split(',')):
                current_api = api
                break
                
        if not current_api:
            current_api = "=_*-default-*_="
        
        response = self.API_USAGE_MAP[current_api](url, save_path)
        
        return
     
    def downloadImgur(self, url, save_path):
        if ".com/a/" in url:
            self.getZipFile(url + "/zip", save_path)
            self.logResponse(2)
            return
        
        try:
            content_type = requests.head(url).headers['Content-Type'].split('/')
        except:
            self.logResponse(-6)
            return
        
        file_extension = f".{content_type[1]}"
        if file_extension == ".*":
            self.logResponse(-2)
            return
        
        if content_type[0] == "image":
            self.getImageFile(url, save_path + file_extension)
            self.logResponse(1)
        elif content_type[0] == "video":
            self.getVideoFile(url, save_path + file_extension)
            self.logResponse(3)
        return
     
    def downloadGfycat(self, url, save_path):
        gfycat_code = url.split('/')[-1]
        try:
            gfycat_query = self.gfycat.query_gfy(gfycat_code)
        except GfycatClientError as e:
            self.logResponse(-3)
            return

        video_url = gfycat_query['gfyItem']['mp4Url']
        self.getVideoFile(video_url, save_path + '.mp4')
        self.logResponse(3)
        return
        
    def downloadReddit(self, url, save_path):
        try:
            content_type = requests.head(url).headers['Content-Type'].split('/')
        except:
            self.logResponse(-6)
            return
        
        file_extension = f".{content_type[1]}"
        if file_extension == ".*":
            self.logResponse(-2)
            return
        
        if content_type[0] == "image":
            self.getImageFile(url, save_path + file_extension)
            self.logResponse(1)
        elif content_type[0] == "video":
            self.getVideoFile(url, save_path + file_extension)
            self.logResponse(3)
        return
        
    def downloadTumblr(self, url, save_path):
        if 've.' in url:
            file_extension = url.split('.')[-1]
            self.getVideoFile(url, save_path + "." + file_extension)
            self.logResponse(3)
        else:
            media_url = url.split('.')[1:]
            media_url = 'https://' + '.'.join(media_url)
            
            try:
                content_type = requests.head(media_url).headers['Content-Type'].split('/')
            except:
                self.logResponse(-6)
                return

            file_extension = f".{content_type[1]}"
            if file_extension == ".*":
                self.logResponse(-2)
                return

            self.getImageFile(url, save_path + file_extension)
            self.logResponse(1)
        return
        
    def downloadTwitter(self, url, save_path):
        status_id = url.split('/')[-1]
        status_media = self.twitter.GetStatus(status_id).media
        
        for media in status_media:
            if media.type == "photo":
                media_url = media.media_url
                
                try:
                    content_type = requests.head(media_url).headers['Content-Type'].split('/')
                except:
                    self.logResponse(-6)
                    continue
                
                file_extension = f".{content_type[1]}" 
                self.getImageFile(media_url, save_path + str(media.id) + file_extension)
                self.logResponse(1)
            elif media.type == "video":
                video_info = media.video_info
                best_bitrate = 0
                video_url = None
                file_extension = None
                
                for variation in video_info['variants']:
                    if not variation.get('bitrate'):
                        self.logResponse(-4)
                        continue
                
                    if variation['bitrate'] > best_bitrate:
                        best_bitrate = variation['bitrate']
                        video_url = variation['url']
                        file_extension = variation['content_type'].split('/')[-1]
                
                if best_bitrate == 0:
                    self.logResponse(-4)
                    continue
                self.getVideoFile(video_url, save_path + "." + file_extension)
                self.logResponse(3)
        return

    def downloadYoutube(self, url, save_path):
        ydl_opts = {
            'quiet': True,
            'outtmpl': f'{save_path}.%(ext)s'
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.logResponse(4)
        except youtube_dl.utils.DownloadError:
            self.logResponse(-8)
        
        return
        
    def ignoreDownload(self, url, save_path):
        self.logResponse(-7)
        return

if __name__ == "__main__":
    image_grabber = ImageGrabber(REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT)
    
    atexit.register(image_grabber.save)
    fire.Fire(image_grabber.getMediaFromList)
