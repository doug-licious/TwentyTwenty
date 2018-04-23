from django.db import models


# Create your models here.

class Desk(models.Model):
    desk_number = models.IntegerField()
    data_points = models.IntegerField(default=6)
    power_points = models.IntegerField(default=10)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.desk_number)
