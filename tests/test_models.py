import pytest
from test_app.models import Question, Answer, TestResult
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_question_model():
    question = Question.objects.create(text="What is the capital of France?")
    assert question.text == "What is the capital of France?"
    assert str(question) == "What is the capital of France?"


@pytest.mark.django_db
def test_answer_model():
    question = Question.objects.create(text="What is the capital of France?")
    answer = Answer.objects.create(question=question, text="Paris", is_correct=True)
    assert answer.text == "Paris"
    assert answer.is_correct
    assert str(answer) == "Paris"


@pytest.mark.django_db
def test_testresult_model():
    user = User.objects.create_user(username="testuser", password="password")
    result = TestResult.objects.create(user=user, score=15)
    assert result.user == user
    assert result.score == 15
