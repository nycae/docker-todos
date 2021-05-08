from django.db import models


class Todo:
    def __init__(self, task, is_finished = False):
        self.task = task
        self.is_finished = is_finished
