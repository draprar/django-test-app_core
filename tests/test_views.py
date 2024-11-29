import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from test_app.models import Question, Answer, TestResult
from django.test import override_settings


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_driving_test_get(client):
    # Simulate HTTPS
    client.defaults['wsgi.url_scheme'] = 'https'

    # Create a user and login
    user = User.objects.create_user(username="testuser", password="password")
    client.login(username="testuser", password="password")

    # Create sample questions and answers
    question1 = Question.objects.create(text="What is 2 + 2?")
    Answer.objects.create(question=question1, text="4", is_correct=True)
    Answer.objects.create(question=question1, text="3", is_correct=False)

    question2 = Question.objects.create(text="What is the capital of France?")
    Answer.objects.create(question=question2, text="Paris", is_correct=True)
    Answer.objects.create(question=question2, text="London", is_correct=False)

    # Perform GET request
    response = client.get(reverse('driving_test'))

    # Assert response and template
    assert response.status_code == 200
    assert 'test_app/driving_test.html' in [t.name for t in response.templates]


from django.test import override_settings

@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=False)  # Disable SSL redirect for testing
def test_driving_test_post(client):
    # Simulate HTTPS
    client.defaults['wsgi.url_scheme'] = 'https'

    # Create a user and login
    user = User.objects.create_user(username="testuser", password="password")
    client.login(username="testuser", password="password")

    # Create sample questions and answers
    question = Question.objects.create(text="What is 2 + 2?")
    correct_answer = Answer.objects.create(question=question, text="4", is_correct=True)
    Answer.objects.create(question=question, text="3", is_correct=False)

    # Perform POST request
    response = client.post(reverse('driving_test'), {'answers': [correct_answer.id]})

    # Assert response and score
    assert response.status_code == 200
    assert "test_app/test_result.html" in [t.name for t in response.templates]
    assert "score" in response.context
    assert response.context["score"] == 1

    # Assert TestResult creation
    result = TestResult.objects.get(user=user)
    assert result.score == 1
