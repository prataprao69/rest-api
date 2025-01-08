from django.urls import path
from myapp.views import StudentsView

urlpatterns=[
    path('home',StudentsView.as_view()),
    path('home/<sid>',StudentsView.as_view()),
]
