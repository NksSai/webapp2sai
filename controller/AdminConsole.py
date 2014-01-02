#!/usr/bin/python
#coding=utf-8
#FILENAME : __AdminConsole.py__ 
#DESCRIBE:

from _tools import *
from webapp2_extras.appengine.users import *

class AdminConsole(webapp2.RequestHandler):
    @admin_required
    def get(self):
        user = users.get_current_user()
        self.response.out.write("hello " + user.nickname())
