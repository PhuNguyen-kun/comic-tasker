from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Events
from comic.models import Panel


@receiver(post_save, sender=Events)
def unlock_comic_panel(sender, instance, **kwargs):
    if instance.completed:
        comic = instance.goal.comic_set.first()  # Assuming one comic per goal
        if comic:
            total_tasks = instance.goal.taskbyai_set.count()
            completed_tasks = instance.goal.events_set.filter(completed=True).count()
            total_panels = comic.panels.count()

            # If it's the last task and not all panels are unlocked, unlock all remaining panels
            if completed_tasks >= total_tasks and total_panels > completed_tasks:
                remaining_locked_panels = comic.panels.filter(unlocked=False)
                for panel in remaining_locked_panels:
                    panel.unlocked = True
                    panel.save()
            else:
                # Otherwise, unlock just one panel in order
                locked_panel = comic.panels.filter(unlocked=False).first()
                if locked_panel:
                    locked_panel.unlocked = True
                    locked_panel.save()
