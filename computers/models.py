from django.db import models
from desks.models import Desk


# Create your models here.


class Computer(models.Model):
    hostname = models.CharField(max_length=10)
    address = models.GenericIPAddressField()
    displays = models.IntegerField(default=2)
    ram = models.IntegerField(default=0)
    cpu = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    desk = models.ForeignKey(Desk, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.hostname


class Software(models.Model):
    version = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    computer = models.ManyToManyField(Computer)

    def __str__(self):
        return self.title
