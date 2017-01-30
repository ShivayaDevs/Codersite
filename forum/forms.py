from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['question', 'ques_category', ]
    widgets = {
    'question': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    }

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['answer', ]
    widgets = {
      'answer': forms.Textarea(attrs={'rows': 13, 'class': 'form-control'})
    }
