#!/usr/bin/python
#FILENAME : ___tools.py__ 
#DESCRIBE:

import sys
sys.path.append("../")

import conf

import webapp2
from google.appengine.ext.webapp import template
import models as md
import json

def get_template(name):
    return conf.TEMPLETE_DIR + name
