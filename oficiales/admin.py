from django.contrib import admin

from .models import *

class Ids(admin.ModelAdmin):
    readonly_fields = ('id', )
# Register your models here.

admin.site.register(Oficiales, Ids)
admin.site.register(Teams)
admin.site.register(Time)
admin.site.register(Calendar)
admin.site.register(Availability)
admin.site.register(NewRecruits)
admin.site.register(Reviews)