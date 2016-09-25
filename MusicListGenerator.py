# coding:utf-8
import requests
from bs4 import BeautifulSoup
import MySQLdb
from Config import Config


class MusicListGenerator:
    ARTIST_ID_UP_LIMIT = 1000000
    ARTIST_BASE_URL = "http://music.163.com/#/artist?id="
    db = MySQLdb.connect ( Config.MYSQL_URL , Config.MYSQL_USERNAME , Config.MYSQL_PASSWORD , Config.MYSQL_DATABASE )
    cursor = db.cursor ( )

    def __get_song_list ( self , artist_page_text ):
        pass

    def __try_artist_id ( self , artist_id ):
        current_url = self.ARTIST_BASE_URL + str ( artist_id )
        page = requests.get ( current_url )
        print page.text
