########### BASE IMPORT ################
from django.conf import settings
import os, sys
from GERPAPI.log import *
########################################
import shutil

import json
from DocCreator.models import Document, GroupField, Field

sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/script"))

PATH_TO_DOCCREATOR = settings.BASE_DIR + "/DocCreator/"

def getDocDict():
    docList=[dirs for root, dirs, files in os.walk(PATH_TO_DOCCREATOR)][1+[dirs for root, dirs, files in os.walk(PATH_TO_DOCCREATOR)][0].index("docs")]
    docDict = {}
    for k in docList:
        docDict[k] = Doc(PATH_TO_DOCCREATOR + "/docs/" + k)
    return docDict

def checkDocMigration(docDict):
    for key, doc in docDict.items():
        if(Document.objects.filter(name = key).count()==0):
            do = Document.objects.create(name=key)
            do.save()
            d = doc.getVar()
            main = GroupField.objects.create(name='main', document=do)
            main.save()
            for key, value in d.items():
                if "type" in d:
                    f = Field.objects.create(name=key, group=main, )
                    f.save()
                else:
                    gf = GroupField.objects.create(name=key, document=do)
                    gf.save()
                    for k, v in value.items():
                        f = Field.objects.create(name=k,group=gf, type=v["type"],choice=v["choices"])
                        f.save()

class Doc:
    def ok(self):
        print("ok")
    def __init__(self, url):
        self.url = url
        self.variable = {}
        self.open()

    def open(self):
        self.file = open(self.url + "/document.tex")
        self.text = self.file.read()
        self.file.close()
        tab = self.text.split("<%")
        for text in tab[1:]:
            name = text.split(":")[0]
            type = text.split(":")[1].split(">")[0]
            if(type=="string"):
                if(len(name.split("_"))>0):
                    if(name.split("_")[0] not in self.variable):
                        self.variable[name.split("_")[0]] = {}
                    self.variable[name.split("_")[0]][name.split("_")[1]] = {"type" : type, "value" : "", "choices":[]}
                else:
                    self.variable[name] = {"type" : type, "value" : ""}
            elif(type=="choice"):
                tab = ">".join(text.split(">")[1:]).split("</%>")[0].split("<:>")
                if(len(name.split("_"))>0):
                    if(name.split("_")[0] not in self.variable):
                        self.variable[name.split("_")[0]] = {}
                    self.variable[name.split("_")[0]][name.split("_")[1]] = {"type" : type, "value" : "", "choices" : tab}
                else:
                    self.variable[name] = {"type" : type, "value" : "", "choices" : tab}

    def getVar(self):
        return self.variable

    def setVar(self, key, value):
        group = ""
        for k in self.variable:
            if key in self.variable[k]:
                group = k
        self.variable[k][key]["value"] = value

    def applyVar(self, filename):
        text = self.text
        for elt in self.text.split("<%")[1:]:
            if(len(elt.split(":"))>1):
                name = elt.split(":")[0]
                if("type" in self.variable[name.split("_")[0]][name.split("_")[1]]):
                    if(self.variable[name.split("_")[0]][name.split("_")[1]]["type"]=="string"):
                        field = "<%" + elt.split(">")[0] + ">"
                        text = text.replace(field,self.variable[name.split("_")[0]][name.split("_")[1]]["value"])
                    elif(self.variable[name.split("_")[0]][name.split("_")[1]]["type"]=="choice"):
                        field = "<%" + elt.split("</%>")[0] + "</%>"
                        text = text.replace(field,">".join(elt.split(">")[1:]).split("<:>")[int(self.variable[name.split("_")[0]][name.split("_")[1]]["value"])].split("</%>")[0])
                else:
                    sub = name.split("_")[0]
                    name = name.split("_")[1]
                    if(self.variable[sub][name.split("_")[0]][name.split("_")[1]]["type"]=="string"):
                        field = "<%" + elt.split(">")[0] + ">"
                        text = text.replace(field,self.variable[sub][name.split("_")[0]][name.split("_")[1]]["value"])
                    elif(self.variable[sub][name.split("_")[0]][name.split("_")[1]]["type"]=="choice"):
                        field = "<%" + elt.split("</%>")[0] + "</%>"
                        text = text.replace(field,">".join(elt.split(">")[1:]).split("<:>")[int(self.variable[sub][name.split("_")[0]][name.split("_")[1]]["value"])].split("</%>")[0])

        f = open(self.url + "/" + filename + ".tex", "w")
        f.write(text)
        f.close()
        os.system("pdflatex -shell-escape -output-directory=" + PATH_TO_DOCCREATOR + "releases -interaction=batchmode -file-line-error " + self.url + "/" + filename + ".tex > /dev/null 2>&1 &")
