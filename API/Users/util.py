from django.shortcuts import render
from django.http import HttpResponse
from Users.models import *
import datetime, hashlib,random
import pytz

def checkToken(request):
    if("Token" in request.POST):
        if(Token.objects.filter(Token=request.POST["Token"]).exists()):
            print(Token.objects.filter(Token=request.POST["Token"]).first().invalidationDate)
            print(datetime.datetime.now())
            if(Token.objects.filter(Token=request.POST["Token"]).first().invalidationDate>datetime.datetime.now(pytz.utc)):
                tok = Token.objects.get(Token=request.POST["Token"])
                tok.invalidationDate = datetime.datetime.now() + datetime.timedelta(hours=1)
                tok.save()
                return True
    return False

def getUser(request):
    if("connToken" in request.COOKIES):
        if(Token.objects.filter(Token=request.COOKIES["connToken"]).exists()):
            if(Token.objects.filter(Token=request.COOKIES["connToken"]).first().invalidationDate>datetime.datetime.now(pytz.utc)):
                tok = Token.objects.get(Token=request.COOKIES["connToken"])
                tok.invalidationDate = datetime.datetime.now() + datetime.timedelta(hours=1)
                tok.save()
                return tok.user
