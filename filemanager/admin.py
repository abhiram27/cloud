from django.contrib import admin
from filemanager.models import *
from django.db import models
for mod in models.Model.__subclasses__():
    try:
        admin.site.register(mod)
        pass
    except:
        pass
