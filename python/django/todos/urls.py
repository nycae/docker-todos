from django.urls import path
from api.views import TodoManager

urlpatterns = [
    path('todo', TodoManager.as_view()),
    path('todo/<int:id>', TodoManager.as_view()),
]
