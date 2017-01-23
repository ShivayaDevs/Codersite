from __future__ import unicode_literals

from django.db import models
from Codersite.models import User

# Create your models here.

class Article(models.Model) :
    article_text = models.CharField(max_length=1000)
    # user = models.ForeignKey(User)