import os, json
from DocCreator.models import *

def info2txt(docName):
    if(Document.objects.filter(name=docName)):
        do = Document.objects.filter(name=docName).first()
        doc = {}
        for k in GroupField.objects.filter(document=do):
            doc[k.name] = {}
            for l in Field.objects.filter(group=k):
                doc[k.name][l.name] = {"type" : l.type, "choice" : l.choice}
        return json.dumps(doc)
    return "no"

def info2json(docName):
    if(Document.objects.filter(name=docName)):
        do = Document.objects.filter(name=docName).first()
        doc = {}
        for k in GroupField.objects.filter(document=do):
            doc[k.name] = {}
            for l in Field.objects.filter(group=k):
                doc[k.name][l.name] = {"type" : l.type, "choice" : l.choice}
        return doc
    return {}
