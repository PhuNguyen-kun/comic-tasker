from django.contrib import admin

from .models import Goal #goal table (goalテーブル)
from .models import Task
from comic.models import Comic
from comic.models import Panel #panel table (panle　テーブル)
from goal.models import TaskByAI #task_by_AI tabel (task_by_AI テーブル)

admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(Comic)
admin.site.register(TaskByAI)
admin.site.register(Panel)

# Register your models here.
