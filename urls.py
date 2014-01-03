#!/usr/bin/python
#coding=utf-8

#FILENAME : __urls.py__ 
#DESCRIBE:

from controllers import *

urlpatterns = [
        (r'^/$', MainPage),
        (r'^/admin/{0,1}$', AdminConsole),
        (r'^/register/{0,1}$', Register),
        ]
