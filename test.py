#coding:utf-8
from Music163API import Music163Api
def test2():
    apis=Music163Api()
    apis.get_songs_of_artist(1071081)
def test3():
    apis=Music163Api()
    apis.get_song_detail(11362719)


if __name__=='__main__':
   test3()