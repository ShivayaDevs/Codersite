from __future__ import unicode_literals
from users.models import User 
from django.db import models

# Create your models here.
class Sample(models.Model):
  username = models.ForeignKey("users.User", verbose_name="users", related_name="User")
  name = models.CharField(max_length=20)
    
    
    