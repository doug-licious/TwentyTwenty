from django.db import models


# from adaptor.model import CsvModel

# Create your models here.

class Room(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.description)


class Desk(models.Model):
    desk_number = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    data_points = models.IntegerField(default=6)
    power_points = models.IntegerField(default=10)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.desk_number)


class Computer(models.Model):
    hostname = models.CharField(max_length=10, primary_key=True)
    address = models.GenericIPAddressField()
    displays = models.IntegerField(default=2)
    ram = models.IntegerField(default=0)
    cpu = models.CharField(max_length=10)

    desk = models.ForeignKey(Desk, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.hostname)


class Software(models.Model):
    version = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50)
    #vendor = models.CharField(max_length=50)

    #computer = models.ManyToManyField(Computer)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)


class DRUser(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    username = models.CharField(max_length=8, primary_key=True)
    business_unit = models.CharField(max_length=5)

    desk = models.ForeignKey(Desk, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.username)
