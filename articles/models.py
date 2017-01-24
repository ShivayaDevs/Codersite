from __future__ import unicode_literals

from django.db import models
from users.models import User


# Create your models here.

class Article(models.Model) :
    content = models.TextField(null = False, default = "text")
    title = models.TextField(null = False, default = "text")
    user = models.ForeignKey(User, default=True)
    date_added = models.DateTimeField(null = False, verbose_name = "date_added")

    def __str__(self):
        return self.title + ", Date Added : " + str(self.date_added)