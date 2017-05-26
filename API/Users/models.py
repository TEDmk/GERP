from django.db import models

# Create your models here.

class User(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200,blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    def isAdmin(self):
        return level>1
    def isManager(self):
        return level>0

class Client(models.Model):
    def __str__(self):
        return self.society
    society = models.CharField(max_length=200)
    siret = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    context = models.CharField(max_length=200)
    time = models.DateField(auto_now=True)



class Token(models.Model):
    def __str__(self):
        return self.user.username
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Token = models.CharField(max_length=200)
    invalidationDate = models.DateTimeField()

class LogData(models.Model):
    def __str__(self):
        if self.user!=None:
            return "[" + str(self.time) + "] " + self.user.username + " : " + self.action

    user = models.ForeignKey(User, default=None, blank=True)
    time = models.DateTimeField(auto_now=True)
    action = models.CharField(max_length=255)
    title = models.CharField(max_length=200, blank=True)
