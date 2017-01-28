from django.contrib import admin
from .models import Category, Question, UserSolution

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(UserSolution)