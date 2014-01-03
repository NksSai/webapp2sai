#!/usr/bin/python
#coding=utf-8
#FILENAME : __mail.py__ 
#DESCRIBE:

from google.appengine.api import mail
import time
import md5
import random
import conf

def send_comform_email(dict):
    if "body" not in dict.keys():
        raise ValueError("email format error")
    return mail.send_mail(dict["mail"], dict["sendto"], dict['subject'], dict["body"])

def creat_conform_id(sender):
    seed = str(random.randint(0,10000))
    timestamp = str(int(time.time()))
    hash = md5.md5()
    hash.update(sender + seed + timestamp)
    return hash.hexdigest()
