from django.urls import path
from qv1.views import QuizView

urlpatterns = [
    path('quizes/', QuizView.as_view(), name="quizes"),

]
