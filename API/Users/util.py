from django.shortcuts import render
from django.http import HttpResponse
from Users.models import *
import datetime, hashlib,random
import pytz

def checkToken(request):
    if("Token" not in request.POST):
        return False
    if not Token.objects.filter(Token=request.POST["Token"]).exists():
        return False
    return True

def getUser(request):
    if("Token" in request.POST):
        if(Token.objects.filter(Token=request.POST["Token"]).exists()):
            if(Token.objects.filter(Token=request.POST["Token"]).first().invalidationDate>datetime.datetime.now(pytz.utc)):
                tok = Token.objects.get(Token=request.POST["Token"])
                tok.invalidationDate = datetime.datetime.now() + datetime.timedelta(hours=1)
                tok.save()
                return tok.user
