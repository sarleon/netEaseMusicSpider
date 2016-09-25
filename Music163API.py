#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
from json import JSONDecoder
class Music163Api:
    cookies={'appver':'1.5.0.75771'}
    headers={
            'Referer': 'http://music.163.com/'
        }


    """
    搜索的api
    s: 搜索
    limit: 返回数量
    sub: 意义不明(非必须参数)；取值：false
    type: 搜索类型；取值意义
    1 单曲
    10 专辑
    100 歌手
    1000 歌单
    1002 用户
    offset: 偏移数量，用于分页
    MUSIC_U: 意义不明(非必须参数)
    """
    def searching(self,song_name):
        cookies={'appver':'1.5.0.75771'}
        headers={
            'Referer': 'http://music.163.com/'
        }
        url="http://music.163.com/api/search/get/"
        data={
            's':song_name,
            'type':1,
            'offset':'0'
        }
        page=requests.post(url=url,data=data,cookies=self.cookies,headers=self.headers)
        print page.content
        return  page



    """
    获取一个歌手的专辑列表
    artist_id是歌手的id

    """
    def get_albums_of_artist(self,artist_id):
        cookies={'appver':'1.5.0.75771'}
        headers={
            'Referer': 'http://music.163.com/'
        }
        url="http://music.163.com/api/artist/"+str(artist_id)+"/"
        data={
            'limit':10,
            'offset':'0'
        }
        page=requests.get(url=url,data=data,cookies=self.cookies,headers=self.headers)
        print page.content

        return  page