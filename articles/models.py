from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model) :
    content = models.TextField(null = False)
    title = models.TextField(null = False)
    user = models.ForeignKey(User, default=True)
    date_added = models.DateTimeField(null = False, verbose_name = "date_added")

    def __str__(self):
        return self.title + ", Date Added : " + str(self.date_added)