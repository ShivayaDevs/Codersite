from django.db import models
from users.models import User


class Category(models.Model):
  name = models.TextField(max_length=100)

  def __str__(self):
    return self.name


class Question(models.Model):
  title = models.TextField(max_length=400)
  statement = models.TextField()
  category = models.ForeignKey(Category)

  def __str__(self):
    return self.title


class UserQuestion(models.Model):
  user = models.ForeignKey(User)
  question = models.ForeignKey(Question)
  solution = models.TextField()
