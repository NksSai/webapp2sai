#!/usr/bin/python
#coding=utf-8

#FILENAME : __urls.py__ 
#DESCRIBE:

from controllers import *

urlpatterns = [
        (r'^/$', MainPage),
        (r'^/admin/$', AdminConsole),
        (r'^/register/$', Register),
        ]
