from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)  # Thêm trường này để theo dõi trạng thái hoàn thành

    class Meta:
        db_table = "tblevents"

    def __str__(self):
        return self.name
