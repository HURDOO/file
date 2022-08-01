from django.db import models


class Upload(models.Model):
    code = models.IntegerField()
    index = models.TextField()
    file = models.FileField(upload_to='')
    time = models.DateTimeField(auto_now=True)
