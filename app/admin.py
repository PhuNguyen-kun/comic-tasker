from django.contrib import admin

<<<<<<< HEAD
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
=======
from goal.models import Goal #goal table (goalテーブル)
from .models import Task #task table (taskテーブル)
from goal.models import TaskByAI #task_by_AI tabel (task_by_AI テーブル)
#from .models import Comic #comic table (comic テーブル)
#from .models import Panel #panel table (panle　テーブル)
admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(TaskByAI)
#admin.site.register(Comic)
#admin.site.register(Panel)
>>>>>>> 9572eef995bfa3449a74d9d0f555af701a35ddf0
