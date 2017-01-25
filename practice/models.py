from django.db import models

class Category(models.Model):
  name = models.TextField(max_length=100)
  
  def __str__(self):
    return self.name

class Question(models.Model):
  title       = models.TextField(max_length=400)
  statement   = models.TextField()
  category    = models.ForeignKey(Category)
  input_file  = models.TextField(max_length=100)
  output_file = models.TextField(max_length=100)
  # input_file : input file's name
  # output_file: output file's name

  def __str__(self):
    return self.title