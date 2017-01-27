from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Question

class IndexView(generic.ListView):
  template_name = 'practice/index.html'
  context_object_name = 'question_list'

  def get_queryset(self):
    return Question.objects.all()

# class DetailView(generic.DetailView):
#   model = Question
#   template_name = 'practice/question_page.html'

class ResultView(generic.DetailView):
  model = Question
  template_name = 'practice/result.html'
    
def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'practice/question_page.html', {
      'question': question,
    }) 
def submit(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  answer = request.POST['answer_input']
  return HttpResponseRedirect(reverse('practice:result', args=(question.id,)))



"""
  1. Add solved by counter
  2. Add sort option
  3. Add solved/not solved

"""    
