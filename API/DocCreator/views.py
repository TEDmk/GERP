from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from Users.util import *
from wsgiref.util import FileWrapper
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/script"))
from doc import *
import os, json
import time
from DocCreator.models import *

from DocCreator.urls import *

from DocCreator.util import *



docDict = getDocDict()
# Create your views here.
def index(request):
    return HttpResponse("", content_type="application/json")

def infogener(request, docDate, docName):
    #if(not checkToken(request)):
    #    return HttpResponse("not_connected", content_type="application/json")
    #us = getUser(request)
    name = docDate + "-" + docName
    if(GeneratedDoc.objects.filter(name=name).exists()):
        gdo = GeneratedDoc.objects.get(name=name)
        r = {}
        r["template"] = gdo.document.name
        r["field"] = {}
        for k in GeneratedKey.objects.filter(generatedDoc=gdo):
            r["field"][k.key] = k.value
        print(r)
        return HttpResponse(json.dumps(r), content_type="application/json")
    else:
        return HttpResponse("not_found", content_type="application/json")

def info(request, docName):
    if(not checkToken(request)):
        return HttpResponse("not_connected", content_type="application/json")
    inf = info2txt(docName)
    return HttpResponse(inf, content_type="application/json")

def add(request, docName):
    if(not checkToken(request)):
        return HttpResponse("not_connected", content_type="application/json")
    us = getUser(request)
    print(docName)
    print(us.username)
    if(Document.objects.filter(name=docName)):
        do = Document.objects.filter(name=docName).first()
        ListOfItems = []
        for k in GroupField.objects.filter(document=do):
            for l in Field.objects.filter(group=k):
                ListOfItems.append(l.name)
        allfield = True
        for x in ListOfItems:
            if x not in request.POST:
                allfield = False
            else:
                if request.POST[x]=="":
                    allfield = False
        if(allfield):
            nam = str(int(time.time()))+"-"+do.name
            Gdo = GeneratedDoc(document=do, name=nam,user=us)
            Gdo.save()
            for x in ListOfItems:
                Gf = GeneratedKey(generatedDoc=Gdo,key=x,value=request.POST[x])
                Gf.save()
            doc = docDict[do.name]
            doc.open()
            for x in ListOfItems:
                doc.setVar(x,request.POST[x])
            doc.applyVar(nam)
            log.add("DocCreator","Creating file : " + nam + ".pdf", us)
            return HttpResponse(nam, content_type="application/json")
        else:
            return HttpResponse("no_all_field", content_type="application/json")
    return HttpResponse("error", content_type="application/json")

def download(request, docDate, docName):
    #if(not checkToken(request)):
    #    return HttpResponse("false", content_type="application/json")
    us = getUser(request)
    file_path = PATH_TO_DOCCREATOR + "/releases/" + docDate + "-" + docName + ".pdf"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/x-pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("not_found", content_type="application/json")

def doclist(request):
    data = list(GeneratedDoc.objects.values('name', 'time', 'user'))
    for x in data:
        x["time"] = x["time"].strftime("%Y-%m-%d")
    return HttpResponse(json.dumps(data), content_type="application/json")

def templatelist(request):
    data = list(Document.objects.values('name'))
    return HttpResponse(json.dumps(data), content_type="application/json")
