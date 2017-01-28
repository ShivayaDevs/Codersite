from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Question, UserSolution
from . import program_executor

class IndexView(generic.ListView):
  template_name = 'practice/index.html'
  context_object_name = 'question_list'

  def get_queryset(self):
    return Question.objects.all()

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  code = """
  #include <iostream>
  using namespace std;
  int main(){

    // your code goes here
    return 0;
  }
  """
  return render(request, 'practice/question_page.html', {
      'question': question,
      'source_code': code,
    })

# How do I get the userID to pass to add_submission_to_db function?
# Basically, how can I get the currently logged in user's ID?
def submit(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  code = request.POST['answer_input']
  result = program_executor.execute_on(code, question.id)
  if result[0] == 0:
    program_executor.cleanup(question.id)
  # FIXME: Unable to get current user's ID, remove the hardcoded '1'.
  add_submission_to_db(1, question.id, code, result[0])
  return render(request, 'practice/question_page.html',{
      'question': question,
      'result_code': result[0],
      'result_message': result[1],
      'source_code': code,
  })

def add_submission_to_db(user_id, question_id, code, status_code):
  UserSolution.objects.create(user_id=user_id, question_id=question_id, solution=code,
                              status_code=status_code, submitted_on=timezone.now())