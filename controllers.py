#!/usr/bin/python
#coding=utf-8
#FILENAME : __controllers.py__ 
#DESCRIBE:

import sys,logging
import os,re
import conf

sys.path.append("./controller/")

#自动从controller中载入模型  
#要求类名称与文件名称一致
#好吧 这不是好习惯 =。= 就是感觉这样比较舒服一点
#ps.我不会java

str_p = r'^(?P<pack>[a-zA-Z]*)\.py$'
pattern = re.compile(str_p)
thismod = sys.modules[__name__]
for name in os.listdir(conf.BASE_DIR + os.sep + "controller"):
    try:
        if pattern.match(name):
            print name
            pack = pattern.match(name).group("pack")
            msg =  "from " + pack + " import " + pack
            logging.log(logging.DEBUG, msg)
            exec("from " + pack + " import " + pack)
    except:
        logging.exception("import " + pack + " error")
