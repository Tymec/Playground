import os
import fire
import glob
import json
import eyed3
from pydub import AudioSegment
from tinytag import TinyTag


def change_song_format(song_path):
    print(f"Processing: {song_path}")
    _noext, song_format = os.path.splitext(song_path)
    song_format = song_format[1:]
    new_path = _noext + ".mp3"

    tags = get_tags_from_song(song_path)
    with open('cover.png', 'wb') as f:
        f.write(tags.get_image())
    
    out_audio = AudioSegment.from_file(song_path, format=song_format)
    out_audio.export(new_path, format="mp3", bitrate=f"{int(tags.bitrate)}k")
    
    modify_song(new_path, tags, "cover.png")
    
    #os.remove(song_path)
    os.rename(song_path, "C:\\Users\\Tymec\\Downloads\\out\\" + _noext.split("\\")[-1] + "." + song_format)
    return

def get_tags_from_song(song_path):
    tags = TinyTag.get(song_path, image=True)
    return tags

def modify_song(song_path, tags, cover_art_path):
    audiofile = eyed3.load(song_path)
    audiofile.initTag()
    audiofile.tag.artist = tags.artist
    audiofile.tag.album = tags.album
    audiofile.tag.album_artist = tags.albumartist
    audiofile.tag.title = tags.title
    audiofile.tag.genre = tags.genre
    audiofile.tag.composer = tags.composer
    if tags.track:
        audiofile.tag.track_num = f"{tags.track}/{tags.track_total}"
    if tags.year:
        audiofile.tag.year = tags.year
    audiofile.tag.disc_num = "1/1"
    audiofile.tag.images.set(3, open(cover_art_path, 'rb').read() , "image/png")
    audiofile.tag.save()
    return
    
def get_all_songs_from_extension(path, ext, new_path="C:\\Users\\Tymec\\Downloads\\m4a\\"):
    for file_path in glob.glob(path + "**", recursive=True):
        _x, extension = os.path.splitext(file_path)
        if not extension == ext:
            continue
        
        filename = _x.split("\\")[-1]
        subfolder = _x.split("\\")[-2]
        if subfolder == "Music":
            subfolder = "Single"
        
        song_info = {
            "title": filename,
            "album": subfolder,
            "path": file_path
        }
        
        album_folder = new_path + subfolder
        if not os.path.isdir(album_folder):
            os.mkdir(album_folder)
        
        os.rename(file_path, album_folder + "\\" + filename + extension)
    return

def loop_over_songs_in_folder(folder_path, extension=".m4a"):
    for song in glob.glob(folder_path + "**", recursive=True):
        _x, _ext = os.path.splitext(song)
        if not _ext == extension:
            continue
        change_song_format(song)

def main():
    #fire.Fire(modify_song)
    #fire.Fire(get_all_songs_from_extension)
    #fire.Fire(change_song_format)
    fire.Fire(loop_over_songs_in_folder)
    
if __name__ == "__main__":
    main()