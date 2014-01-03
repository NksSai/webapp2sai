#!/usr/bin/python
#FILENAME : __Register.py__ 
#DESCRIBE:

from _tools import *

class Register(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("ok")

    def post(self):
        email = self.request.POST['email']
        name = self.request.POST['name']
        passwd = self.request.POST['passwd']
        user = md.CheckUser(email, name, passwd)
        ans = {}
        if user.register():
            ans['ret'] = '1'
        else:
            ans['ret'] = '0'

        return self.response.out.write(json.dumps(ans))
