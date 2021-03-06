import os, sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/script"))
from django.conf.urls import url,include
from django.contrib import admin

from . import views

from doc import *

docDict = getDocDict()
checkDocMigration(docDict)
print("ok")

urlpatterns = [
    url(r'info/(?P<docName>\w+)', views.info, name="info"),
    url(r'doclist', views.doclist, name="info"),
    url(r'templatelist', views.templatelist, name="info"),
    url(r'add/(?P<docName>\w+)', views.add, name="add"),
    url(r'generate/download/(?P<docDate>\w+)-(?P<docName>\w+)', views.download, name="download"),
    url(r'generate/infod/(?P<docDate>\w+)-(?P<docName>\w+)', views.infogener, name="infogener"),
    url(r'^$', views.index, name='index'),
]
