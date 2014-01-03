#!/usr/bin/python
#FILENAME : __Register.py__ 
#DESCRIBE:

from _tools import *

class Register(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("ok")

    def post(self):
