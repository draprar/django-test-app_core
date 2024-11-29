
from django.contrib import admin
from .models import Question, Answer, TestResult

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestResult)
            