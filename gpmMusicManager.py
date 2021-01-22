from gmusicapi import Musicmanager

class MusicManager:
    def __init__(self):
        self.mm = Musicmanager()
        #self.mm.perform_oauth()
        self.mm.login()
        
    def upload_songs(self, filepath):
        new_filepaths = []
        # Get every song from filepath
        # Loop over every song add non-MP3 files into a list
        # Convert non-MP3 files into MP3
        
        self.mm.upload(new_filepaths)
        
if __name__ == "__main__":
    musicMan = MusicManager()
    musicMan.upload_songs("E:\Music\")
    
