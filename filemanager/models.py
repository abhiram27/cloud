from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class File(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="imgs")
    deleted = models.BooleanField(blank=True, null=True,default=False)
    created = models.DateTimeField(blank=True, default=timezone.now)
    class Meta:
        managed = True
        db_table = 'File'


class Filexuser(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', blank=True, null=True)
    file = models.ForeignKey(File, models.DO_NOTHING, db_column='file', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FileXUser'

class OptionMenu(models.Model):
    option=models.CharField(max_length=20)
    class Meta:
        managed = True
        db_table = 'optionMenu'