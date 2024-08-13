from django.db import models

class Goal(models.Model): #goal table (goalテーブル)
    goal_id = models.AutoField(primary_key=True)
    goal_name = models.CharField(max_length=255)
    start_day = models.DateField()
    finish_day = models.DateField()

    def __str__(self):
        return self.goal_name

from .models import Goal #task table (taskテーブル)
class Task(models.Model): 
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    cmopleted = models.BooleanField(default=False)
    goal = models.Foreignkey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

from .models import Goal #comic table (comic テーブル)
from .models import Task
class Comic(models.Model): 
    comic_id = models.AutoField(primary_key=True)
    comic_img = models.CharField(max_length=255)
    number_of_panel = models.CharField(max_length=255)
    unlocked = models.BooleanField(default=False)
    task = models.Foreignkey(Task, on_delete=models.CASCADE)
    goal = models.Foreignkey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.comic_img

from .models import Goal #task_by_AI tabel (task_by_AI テーブル)
class TaskByAI(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    deadline = models.DateField()
    goal = models.Foreignkey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name

from .models import Comic #panel table (panle　テーブル)
class Panel(models.Model):
    panel_id = models.AutoField(primary_key=True)
    comic_panel = models.CharField(max_length=255)
    panel_img = models.CharField(max_length=255)
    unlocked = modelse.BooleanField(default=False)
    comic = models.Foreignkey(Comic, on_delete=models.CASCADE)
# Create your models here.

# Create your models here.
