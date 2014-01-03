#!/usr/bin/python
#coding=utf-8

#FILENAME : __url_test.py__ 
#DESCRIBE:

import cookielib
import urllib,urllib2


def init():
    cookie = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)

def data_post(url, post_dic):
    req = urllib2.Request(url, urllib.urlencode(post_dic))
    return urllib2.urlopen(req).read()

def data_get(url, get_dic = ''):
    req = urllib2.Request(url +"?" +urllib.urlencode(get_dic))
    return urllib2.urlopen(req).read()

init()
