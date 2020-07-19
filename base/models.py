from django.db import models

# Create your models here.
class Datas(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='images')
    pdf = models.FileField(upload_to='files')
    desc = models.TextField()
    permission = models.BooleanField(default=False)
    