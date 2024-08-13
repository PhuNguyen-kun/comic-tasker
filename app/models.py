from django.db import models

class Goal(models.Model): #goal table (goalテーブル)
    goal_id = models.AutoField(primary_key=True) #goal's id(goalのid)
    goal_name = models.CharField(max_length=255) #goal's name(goalの名前)
    start_day = models.DateField() #startday (開始日)
    finish_day = models.DateField() #finishday(終了日)
    number_of_task = models.CharField(max_length=255) #number of task (taskの数)

    def __str__(self):
        return self.goal_name

from .models import Goal #to use goal_id (gaol_idを使うため)
class Task(models.Model): #task table (taskテーブル) 
    task_id = models.AutoField(primary_key=True) #task's id (taskのid)
    task_name = models.CharField(max_length=255) #task's name (taskの名前)
    completed = models.BooleanField(default=False) #Is the task completed? (taskが完了しているか)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.task_name

from .models import Goal #to use goal_id (gaol_idを使うため)
from .models import Task #to use task_id (task_idを使うため)
class Comic(models.Model):  #comic table (comic テーブル)
    comic_id = models.AutoField(primary_key=True) #comic's id (comicのid)
    comic_img = models.CharField(max_length=255) #comic's image (comicの画像)
    number_of_panel = models.CharField(max_length=255) #number of panel[task] (panel[task]の数)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) #ForeignKey form task (taskからの外部キー)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.comic_img

from .models import Goal #to use goal_id (gaol_idを使うため)
class TaskByAI(models.Model): #task_by_AI tabel (task_by_AI テーブル) 
    task_id = models.AutoField(primary_key=True) #task's id (taskのid)
    task_name = models.CharField(max_length=255) #task's name (taskの名前)
    number_of_task = models.CharField(max_length=255) #number of task (taskの数)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from goal (goalからの外部キー)

    def __str__(self):
        return self.task_name

from .models import Comic #to use comic_id (comic_idを使うため)
class Panel(models.Model): #panel table (panle　テーブル)
    panel_id = models.AutoField(primary_key=True) #panel's id (panelのid)
    comic_panel = models.CharField(max_length=255) #panel number (panelの番号)
    panel_img = models.CharField(max_length=255) #panel's image (panelの画像)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE) #ForeignKey from comic (comicからの外部キー)
# Create your models here.