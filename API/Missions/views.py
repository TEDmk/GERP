from django.shortcuts import render
from django.http import HttpResponse
from DocCreator.models import *
from Users.util import *
from Missions.models import *
import json
# Create your views here.

def index(request):
    L = []
    for x in Mission.objects.filter(archived=False).order_by("-lastmodifTime"):
        item = {}
        item["studyName"] = x.name
        item["userInCharge"] = x.user.username
        item["lastmodifTime"] = str(x.lastmodifTime)
        L.append(item)
    return HttpResponse(json.dumps(L), content_type="application/json")


def info(request, name):
    if(not checkToken(request)):
        return HttpResponse("not_connected", content_type="application/json")
    us = getUser(request)
    if(not Mission.objects.filter(name=name)):
        return HttpResponse("mission_not_found", content_type="application/json")
    mission = Mission.objects.filter(name=name).first()
    returnedDic = {}
    fields = MissionField.objects.filter(mission=mission)
    for field in fields:
        returnedDic[field.key] = field.value
    docs = AttachedDoc.objects.filter(mission=mission)
    returnedDic["document"] = {}
    for doc in docs:
        returnedDic["document"][doc.type] = {}
        date = {}
        date["mois"] = doc.activeDate.month
        date["jour"] = doc.activeDate.day
        date["année"] = doc.activeDate.year
        returnedDic["document"][doc.type]["date_signature"] = date
    user = mission.user
    client = mission.client
    returnedDic["nom_etude"] = name
    return HttpResponse(json.dumps(returnedDic), content_type="application/json")
