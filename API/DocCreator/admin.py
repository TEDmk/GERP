from django.contrib import admin
from DocCreator.models import *
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Document,DocumentAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ("group", "name", "type", "choice")
admin.site.register(Field, FieldAdmin)

class GroupFieldAdmin(admin.ModelAdmin):
    list_display = ("document", "name")
admin.site.register(GroupField, GroupFieldAdmin)

class GeneratedDocAdmin(admin.ModelAdmin):
    list_display = ("document", "name", "time", "user")
admin.site.register(GeneratedDoc, GeneratedDocAdmin)

class GeneratedKeyAdmin(admin.ModelAdmin):
    list_display = ("generatedDoc", "key", "value")
admin.site.register(GeneratedKey)
