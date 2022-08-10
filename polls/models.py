from django.db import models


class Upload(models.Model):
    code = models.IntegerField()
    file = models.FileField(upload_to='')
    temporary = models.BooleanField(default=False)

    # use later
    index = models.TextField()
    time = models.DateTimeField(auto_now=True)
