from django.db import models
from .models import*
from django.contrib.auth.models import User
# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rec_name = models.CharField(max_length=100)
    rec_img= models.ImageField(upload_to="receipe")
    rec_desc= models.TextField()
    receipe_view_count= models.IntegerField(default=1)



