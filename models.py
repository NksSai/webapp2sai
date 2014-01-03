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
from tools import mail
import logging
import conf


#从gdb中获得模型，从db中获取处理工具
#好吧 这样的设计肯定有问题 =。=
class CheckUser(gdb.Model):

    def __init__(self, email, passwd = None, nick_name = None, thisdb = None):
        #TODO 数据格式检查
        self.real_db = thisdb
        self.email = email
        self.passwd = passwd
        self.nick_name = nick_name

    def register(self):
        #目前没发现能把非祖先查询和更新放在一起原子操作的方法
        #TODO 以下操作应该是原子的
        return self.register_inernal()

    @staticmethod
    def check_used(type, value):
        query = gdb.User_DB.all()
        query.filter(type + " = " ,value)
        result = query.fetch(5)
        if len(result) > 0:
            return True
        else:
            return False

    def register_inernal(self):
        if CheckUser.check_used("email", self.email):
            logging.debug("email :" + self.email + " is used")
            return False
        else:
            self.real_db = gdb.User_DB(email = self.email, passwd = self.passwd, nick_name = self.nick_name)
            id = mail.creat_conform_id(self.email)
            dict = {}
            dict['mail'] = conf.ADMIN_EMAIL
            dict['subject'] = "comform your register"
            dict["sendto"] = self.email
            from google.appengine.ext.webapp import template
            url = conf.BASE_URL + "/register?key=" + id
            dict['body'] = template.render(conf.TEMPLETE_DIR+"email.html", \
                    {'url':url})
            self.real_db.put()
            comform = gdb.EmailCheck( hash_id = id, ref = self.real_db.key())
            comform.put()
            mail.send_comform_email(dict)
            logging.log(logging.DEBUG, "send mail to " + self.email)
            return True

    def store(self):
        query = gdb.User_DB.all()
        if not self.email:
            return False
        query.filter("email = ", self.email)
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

