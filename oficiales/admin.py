from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Oficiales)
admin.site.register(Teams)
admin.site.register(Time)
admin.site.register(Calendar)
admin.site.register(Availability)
admin.site.register(NewRecruits)
admin.site.register(Reviews)