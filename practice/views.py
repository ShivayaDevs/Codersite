from django.shortcuts import render
from django.views import generic
from .models import Category, Question

class IndexView(generic.ListView):
  template_name = 'practice/index.html'
  context_object_name = 'question_list1'

  def get_queryset(self):
    return Question.objects.all()

class DetailView(generic.DetailView):
  model = Question
  template_name = 'practice/question_page.html'

class ResultView(generic.DetailView):
  model = Question
  template_name = 'practice/result.html'
    



"""
  1. Add solved by counter
  2. Add sort option
  3. Add solved/not solved

"""    
