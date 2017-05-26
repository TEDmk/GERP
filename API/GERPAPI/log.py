import datetime
import time
from django.conf import settings
from django.db import models
from Users.models import User,LogData


class Log:
    def __init__(self):
        self.docname = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    def silent(self, title, text, user=None, tim=0):
        if(tim==0):
            tim = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.doc = open(settings.BASE_DIR + "/log/" + self.docname + ".txt", "w")
        log = LogData(user=user,action=text,title=title)
        log.save()
        self.doc.write("[" + str(tim) + "] " + user.username + " : " + title +  " : " + text)
        self.doc.close()

    def add(self, title, text, user=None):
        tim = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("[" + str(tim) + "] " + user.username + " | " + title +  " : " + text)
        self.silent(title, text, user, time)

log = Log()
