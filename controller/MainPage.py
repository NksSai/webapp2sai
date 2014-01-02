#!/usr/bin/python
#coding=utf-8
#FILENAME : __MainPage.py__ 
#DESCRIBE:

from _tools import * 

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.out.write(get_template("impress.html")) 
        self.response.out.write(template.render(get_template("impress.html"),{}))
