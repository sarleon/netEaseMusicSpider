# coding:utf-8
import requests
from bs4 import BeautifulSoup
import MySQLdb
from Config import Config
from Music163API import Music163Api


class MusicListGenerator:
    ARTIST_ID_UP_LIMIT = 1000000

    def __init__(self):
        db = MySQLdb.connect ( Config.MYSQL_URL , Config.MYSQL_USERNAME , Config.MYSQL_PASSWORD , Config.MYSQL_DATABASE )
        cursor = db.cursor ( )
        self.api=Music163Api()

    def __get_song_list ( self , artist_page_text ):
        pass

    def __try_artist_id ( self , artist_id ):
        return self.api.get_songs_of_artist(artist_id)

if __name__ == '__main__':
    mlg=MusicListGenerator()
