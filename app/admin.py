from django.contrib import admin

from .models import Goal #goal table (goalテーブル)

admin.site.register(Goal)

from .models import Task #task table (taskテーブル)

admin.site.register(Task)

from .models import Comic #comic table (comic テーブル)

admin.site.register(Comic)

from .models import TaskByAI #task_by_AI tabel (task_by_AI テーブル)

admin.site.register(TaskByAI)

from .models import Panel #panel table (panle　テーブル)

admin.site.register(Panel)

# Register your models here.
