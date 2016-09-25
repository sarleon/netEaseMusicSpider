#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
class Music163Api:
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
        page=requests.post(url=url,data=data,cookies=cookies,headers=headers)
        return  page
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
        page=requests.post(url=url,data=data,cookies=cookies,headers=headers)
        return  page