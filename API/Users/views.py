from django.shortcuts import render
from django.http import HttpResponse
from Users.models import *
import datetime, hashlib,random
import pytz
# Create your views here.
from Users.util import *
import json

def index(request):
    if("Token" not in request.POST):
        return HttpResponse(json.dumps({"status" : 401}), content_type="application/json")
    if not Token.objects.filter(Token=request.POST["Token"]).exists():
        return HttpResponse(json.dumps({"status" : 401}), content_type="application/json")

    us = Token.objects.filter(Token=request.POST["Token"]).first().user
    user = {}
    user["username"] = us.username
    user["firstname"] = us.firstname
    user["lastname"] = us.lastname
    user["email"] = us.email
    user["cellphone"] = us.cellphone
    user["type"] = us.type
    user["level"] = us.level
    return HttpResponse(json.dumps(user), content_type="application/json")

def getUser(request):
    return HttpResponse(json.dumps(list(User.objects.values('username', 'email', 'cellphone', 'level'))), content_type="application/json")

def getClient(request):
    data = list(Client.objects.values('firstname', 'surname', 'society', 'siret', 'cellphone', 'email', 'context', 'time'))
    for x in data:
        x["time"] = x["time"].strftime("%Y-%m-%d")
    return HttpResponse(json.dumps(data), content_type="application/json")


def connection(request):
    print(request.POST)
    if(checkToken(request)):
        print(request.COOKIES)
        tok = request.COOKIES["connToken"]
        r = {}
        r["status"] = 200
        r["body"] = {"token" : tok}
        return HttpResponse(json.dumps(r), content_type="application/json")
    if("username" in request.POST and "password" in request.POST):
        psswd = hashlib.sha224(request.POST["password"].encode()).hexdigest()
        if(User.objects.filter(username=request.POST['username'],password=psswd).exists()):
            tok = hashlib.md5(str(random.random()).encode()).hexdigest()
            tk = Token(Token=tok,user=User.objects.filter(username=request.POST['username'],password=psswd).first(),invalidationDate=datetime.datetime.now() + datetime.timedelta(hours=1))
            tk.save()
            r = {}
            r["status"] = 200
            r["body"] = {"token" : tok}
            resp = HttpResponse(json.dumps({"token" : tok}), content_type="application/json")
            resp.set_cookie("connToken", tok)
            return resp
    return HttpResponse(json.dumps({"status" : 200}), content_type="application/json")
