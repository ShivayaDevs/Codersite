from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Question
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

def submit(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  code = request.POST['answer_input']
  result = program_executor.execute_on(code, question.id)
  if result[0] == 0:
    program_executor.cleanup(question.id)
  # TODO: Store the result code in the UserQuestion mapping along with the solution
  return render(request, 'practice/question_page.html',{
      'question': question,
      'result_code': result[0],
      'result_message': result[1],
      'source_code': code,
  })
