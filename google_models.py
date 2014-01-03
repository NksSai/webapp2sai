#!/usr/bin/python
#coding=utf-8
#FILENAME : __google_models.py__ 
#DESCRIBE:

import logging
from google.appengine.ext import db

class User_DB(db.model):
    email = db.EmailProperty(required = True)
    passwd = db.StringProperty(required = True)
    nick_name = db.StringProperty(required = True)
    status = db.BooleanProperty(required = True, default = False)


class Model():
    #现在这样实现仍然不能对DB以及DB_Controller解耦合
    #暂时没想到什么好的方法
    #先这样用
    #TODO 这部分应该重构 以脱离google_models这个包的组合
    def __init__(self, thisdb = None):
        self.real_db = thisdb

    def insert(self):
        if not self.real_db:
            logging.log(logging.WARNING, "db is None")
            raise UnboundLocalError("db is None")
        real_db.put()

    def store():
        raise NotImplementedError("store not impemented")
