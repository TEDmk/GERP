from django.contrib import admin
from Users.models import *
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ("society", "surname", "firstname", "cellphone", "email", "context", "time")
admin.site.register(Client, ClientAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "cellphone", "level")
admin.site.register(User, UserAdmin)

class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "Token", "invalidationDate")
admin.site.register(Token, TokenAdmin)

class LogDataAdmin(admin.ModelAdmin):
    list_display = ("user", "time", "title", "action")
admin.site.register(LogData, LogDataAdmin)
