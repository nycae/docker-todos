from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

import json


class TodoManager(APIView):
    todos = []

    def get(self, request, id=None):
        data=self.todos if id is None else self.todos[id]
        return JsonResponse(data=data, encoder=TodoSerializer, safe=False)

    def post(self, request, id=None):
        if id is None:
            if not request.data or not "task" in request.data:
                return Response(status=400)
            todo = Todo(request.data['task'])
            self.todos.append(todo)
        else:
            if not request.data or not "is_finished" in request.data:
                return Response(status=400)
            todo = self.todos[id]
            todo.is_finished = request.data['is_finished']
        return JsonResponse(data=todo, encoder=TodoSerializer, safe=False)
