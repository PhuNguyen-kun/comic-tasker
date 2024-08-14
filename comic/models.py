from django.db import models

from app.models import Goal #to use goal_id (gaol_idを使うため)
#from app.models import Task #to use task_id (task_idを使うため)

class Comic(models.Model):  #comic table (comic テーブル)
    comic_img = models.CharField(max_length=255) #comic's image (comicの画像)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) #ForeignKey from gaol (goalからの外部キー)

    def __str__(self):
        return self.comic_img
    

class Panel(models.Model): #panel table (panle　テーブル)
    panel_img = models.CharField(max_length=255) #panel's image (panelの画像)
    unlocked = models.BooleanField(default=False) #Is the panel opened? (panelが開いているか)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE) #ForeignKey from comic (comicからの外部キー)

    def __str__(self):
        return self.panel_img
    