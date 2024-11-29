from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, TestResult
import random


@login_required
def driving_test(request):
    if request.method == "POST":
        selected_answers = request.POST.getlist('answers')
        correct_answers = Answer.objects.filter(is_correct=True).values_list('id', flat=True)
        score = sum(1 for ans_id in selected_answers if int(ans_id) in correct_answers)
        TestResult.objects.create(user=request.user, score=score)
        return render(request, 'test_app/test_result.html', {'score': score})

    questions = list(Question.objects.all())
    random.shuffle(questions)
    questions = questions[:20]
    return render(request, 'test_app/driving_test.html', {'questions': questions, 'timer': 1200})
