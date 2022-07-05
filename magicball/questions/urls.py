from django.urls import path

from questions.views import AnswerView, LoginView, RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_token'),
    path('register/', RegisterView.as_view(), name='register'),
    path('getanswer/', AnswerView.as_view(), name='getanswer'),
]
