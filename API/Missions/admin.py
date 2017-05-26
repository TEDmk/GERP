from django.contrib import admin
from Missions.models import *


# Register your models here.
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name","user","client","createdTime")
admin.site.register(Mission,MissionAdmin)

class AttachedDocAdmin(admin.ModelAdmin):
    list_display = ("mission","uploadedTime","selected","generatedDoc", "urlDoc")
admin.site.register(AttachedDoc,AttachedDocAdmin)

class MissionFieldAdmin(admin.ModelAdmin):
    list_display = ("mission","key","value","createdTime", "selected")
admin.site.register(MissionField,MissionFieldAdmin)
