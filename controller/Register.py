#!/usr/bin/python
#coding=utf-8
#FILENAME : __Register.py__ 
#DESCRIBE:

from _tools import *

class Register(webapp2.RequestHandler):
    def check_mail():
        try:
            #TODO 又是一个应该是原子的操作
            key = self.request.GET['key']
            checker = md.EmailCheck(hash_id = key)
            checker.store()
            user = checker.return_ref()
            checker.delete()
            user.update_status(True)
            return True
        except:
            return False

    def get(self):
        if "key" in self.request.GET.keys():
            try:
                key = self.request.GET['key']
                checker = md.EmailCheck(hash_id = key)
                checker.store()
                user = checker.return_ref()
                checker.delete()
                user.update_status(True)
                ans = {"ret":'1'}
                self.response.out.write(json.dumps(ans))
            except:
                ans = {"ret":'0'}
                self.response.out.write(json.dumps(ans))
        else:
            #TODO 这种不应该访问的页面应该统一
            self.response.out.write("error")

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
