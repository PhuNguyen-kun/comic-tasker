from django.db import models
<<<<<<< HEAD
from django.utils import timezone

class Goal(models.Model): #goal table (goalテーブル )
    goal_name = models.CharField(max_length=255)
    start_day = models.DateField(default=timezone.now)
    finish_day = models.DateField()
    number_of_task = models.IntegerField()
    ai_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.goal_name

=======
from goal.models import Goal

>>>>>>> 9572eef995bfa3449a74d9d0f555af701a35ddf0
class Task(models.Model): #task table (taskテーブル) 
    task_name = models.CharField(max_length=255) #task's name (taskの名前)
    completed = models.BooleanField(default=False) #Is the task completed? (taskが完了しているか)
    start_day=models.DateTimeField(default=timezone.now)
    deadline=models.DateTimeField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.task_name
<<<<<<< HEAD
=======

'''
from goal.models import Goal #to use goal_id (gaol_idを使うため)
from app.models import Task #to use task_id (task_idを使うため)
class Comic(models.Model):  #comic table (comic テーブル)
    comic_id = models.AutoField(primary_key=True) #comic's id (comicのid)
    comic_img = models.CharField(max_length=255) #comic's image (comicの画像)
    number_of_panel = models.CharField(max_length=255) #number of panel[task] (panel[task]の数)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) #ForeignKey form task (taskからの外部キー)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.comic_img
class Panel(models.Model): #panel table (panelテーブル)
    panel_id = models.AutoField(primary_key=True) #panel's id (panelのid)
    comic_panel = models.CharField(max_length=255) #panel number (panelの番号)
    panel_img = models.CharField(max_length=255) #panel's image (panelの画像)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE) #ForeignKey from comic (comicからの外部キー)
# Create your models here.
'''
>>>>>>> 9572eef995bfa3449a74d9d0f555af701a35ddf0
