#!/usr/bin/python
#coding=utf-8
#FILENAME : __StartPage.py__ 
#DESCRIBE:

from _tools import *

class StartPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render(get_template("start.html"),{}))

