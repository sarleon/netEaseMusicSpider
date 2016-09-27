# coding:utf-8
import requests
from bs4 import BeautifulSoup
import MySQLdb
from Config import Config
from Music163API import Music163Api

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class MusicListGenerator:
    ARTIST_ID_UP_LIMIT = 1000000

    def __init__(self):
        self.db = MySQLdb.connect ( Config.MYSQL_URL , Config.MYSQL_USERNAME , Config.MYSQL_PASSWORD , Config.MYSQL_DATABASE,charset="utf8" )
        self.cursor = self.db.cursor ( )
        self.api=Music163Api()

    def handle_song(self,artist_id,song_id):
        song_detail=self.api.get_song_detail(song_id)
        artist_name=song_detail[0]
        song_name=song_detail[1]
        comment_num=self.api.get_song_comments(song_id)
        print "********************************************"
        print artist_id
        print song_id
        print type(artist_name)
        print (song_name)
        print comment_num
        sql="INSERT INTO song(artist_id,id,artist,name,comments ) VALUES (%s,%s,%s,%s,%s)"


        result=self.cursor.execute(sql,(artist_id,song_id,artist_name,song_name,comment_num))
        print result.bit_length()
        try:
            self.db.commit()

        except Exception,e:
            self.db.rollback()
            print e.message
            print "insert error"


    def try_artist_id ( self , artist_id ):
        artist_song_list= self.api.get_songs_of_artist(artist_id)
        for song in artist_song_list:
            try:
                self.handle_song(artist_id,song)
            except:
                print "song:"+str(song)


if __name__ == '__main__':
    mlg=MusicListGenerator()
    for i in range(1800,100000) :
        try:
            mlg.try_artist_id(i)
        except:
            print "singer:"+str(i)
            print "error"