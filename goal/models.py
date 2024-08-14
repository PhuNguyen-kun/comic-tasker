from django.db import models

from app.models import Goal

class TaskByAI(models.Model): #TaskbyAI table (TaskbyAIテーブル)
    task_name = models.CharField(max_length=255)
    start_day = models.DateField()
    deadline = models.DateField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
