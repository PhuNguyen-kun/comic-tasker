from django.db import models
from django.utils import timezone

class Goal(models.Model): #goal table (goalテーブル )
    goal_name = models.CharField(max_length=255)
    start_day = models.DateField(default=timezone.now)
    finish_day = models.DateField()
    number_of_task = models.IntegerField()
    ai_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.goal_name

class Task(models.Model): #task table (taskテーブル) 
    task_name = models.CharField(max_length=255) #task's name (taskの名前)
    completed = models.BooleanField(default=False) #Is the task completed? (taskが完了しているか)
    start_day=models.DateTimeField(default=timezone.now)
    deadline=models.DateTimeField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.task_name
