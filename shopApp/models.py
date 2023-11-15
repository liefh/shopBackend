from django.db import models

# Create your models here.

class MenuList(models.Model):
    auth_name = models.CharField(max_length=30,unique=True)
    path = models.CharField(max_length=30,null=True,blank=True)
    is_children = models.BooleanField(default=False)
    parent_id = models.IntegerField(null=True,blank=True)




