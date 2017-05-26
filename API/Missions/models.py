from django.db import models
from Users.models import *
from DocCreator.models import *
from datetime import *
# Create your models here.

class Mission(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    client = models.ForeignKey(Client)
    createdTime = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    lastmodifTime = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name

class AttachedDoc(models.Model):
    mission = models.ForeignKey(Mission)
    type = models.CharField(max_length=200, default="", blank=True)
    uploadedTime = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=True)
    generatedDoc = models.ForeignKey(GeneratedDoc, blank=True)
    urlDoc = models.CharField(max_length=200, default="", blank=True)
    audit = models.BooleanField(default=False)
    activeDate = models.DateTimeField(default=datetime.fromtimestamp(0))

    def __str__(self):
        return self.urlDoc

class MissionField(models.Model):
    mission = models.ForeignKey(Mission)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    createdTime = models.DateTimeField(auto_now=True)
    selected = models.BooleanField(default=True)
