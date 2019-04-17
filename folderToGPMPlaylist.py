import glob
import json
import argparse
from mutagen.easyid3 import EasyID3
from gmusicapi import Mobileclient


parser = argparse.ArgumentParser(description='Folder with music files to a Google Play Music playlist')
parser.add_argument('-f', '--folder', help="Folder with music files", dest="folder", metavar="folder", required=True)
parser.add_argument('-p', '--playlist', help="Playlist name", dest="playlist", metavar="playlist", required=True)
args = vars(parser.parse_args())


def create_playlist(client, name, song_id_list):
    playlist_id = client.create_playlist(name)
    client.add_songs_to_playlist(playlist_id, song_id_list)
    return playlist_id


def song_tags_to_dict(folder_path):
    song_dict = {}
    for song_path in glob.glob(folder_path + "\*"):
        audio = EasyID3(song_path)
        song_dict[song_path] = audio
    return song_dict


def get_song_id_from_song_name(song_info, song_dict):
    if song_info['title'] in [song['title'][0] for song in song_dict.values()]:
        if song_info['artist'] in [song['artist'][0] for song in song_dict.values()]:
            return song_info['id']


def create_all_songs_dictionary(all_songs, song_dict):
    song_id_list = []
    for song in all_songs:
        song_id = get_song_id_from_song_name(song, song_dict)
        if song_id:
            song_id_list.append(song_id)
    return song_id_list


def generate_playlist_from_folder(client, playlist_name, folder_path):
    song_dict = song_tags_to_dict(folder_path)
    song_id_list = create_all_songs_dictionary(client.get_all_songs(), song_dict)
    playlist = create_playlist(client, playlist_name, song_id_list)
    return playlist


if __name__ == "__main__":
    mobile_client = Mobileclient()
    # mobile_client.perform_oauth()
    if mobile_client.oauth_login(Mobileclient.FROM_MAC_ADDRESS):
        generate_playlist_from_folder(mobile_client, args['playlist'], args['folder'])
