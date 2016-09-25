#coding:utf-8
from Music163API import Music163Api
def test():
    apis=Music163Api()
    apis.get_albums_of_artist(3252)



if __name__=='__main__':
   test()