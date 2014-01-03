#!/usr/bin/python
#coding=utf-8
#FILENAME : __models.py__ 
#DESCRIBE:

#这里之所以不用controller的方法，
#我不喜欢模型很复杂
#文件长不要紧  逻辑在一起就好
#我也知道controller那样效率以及习惯不好

import google_models as gdb
from google.appengine.ext import db
import tasks


#从gdb中获得模型，从db中获取处理工具
#好吧 这样的设计肯定有问题 =。=
class CheckUser(gdb.Model):

    def __init__(self, email, passwd = None, nick_name = None, thisdb = None):
        self.real_db = thisdb
        self.email = email
        self.passwd = passwd
        self.nick_name = nick_name

    def register(self):
        return db.run_in_transaction(self.register_inernal)

    @staticmethod
    def check_used(type, value):
        query = gdb.User_DB.all()
        query.filter(type + " = " + str(value))
        result = q.fetch(5)
        if len(result) > 0:
            return True
        else:
            return False

    def register_inernal(self):
        if not CheckUser().check_used("email", self.email):
            return False
        else:
            self.real_db = gdb.User_DB(self.email, self.passwd, self.nick_name)
            self.put()
            return True

    def store(self):
        query = gdb.User_DB.all()
        if not self.email:
            return False
        query.filter("email = " + self.email)
        result = q.fetch(5)
        if len(result) < 0:
            return False
        else:
            p = result[0]
            self.passwd = p.passwd
            self.nick_name = p.nick_name
            self.real_db = p

    def after_checked():
        if not self.real_db:
            if not self.store():
                raise UnbounderLocalError

        self.real_db.status = True
        self.real_db.put()
