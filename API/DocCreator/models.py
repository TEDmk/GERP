from django.db import models
from Users.models import *
# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=200)

class GroupField(models.Model):
    def __str__(self):
        return self.name
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Field(models.Model):
    def __str__(self):
        return self.group.document.name + ":" + self.group.name + ":" + self.name
    group = models.ForeignKey(GroupField, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    choice = models.CharField(max_length=200)

class GeneratedDoc(models.Model):
    def __str__(self):
        return str(self.document.name + ":" + self.name)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time = models.DateField(auto_now=True)
    user = models.ForeignKey(User, default=None)

class GeneratedKey(models.Model):
    def __str__(self):
        return str(self.key)
    generatedDoc = models.ForeignKey(GeneratedDoc, on_delete=models.CASCADE)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    version = models.IntegerField(default=0)
