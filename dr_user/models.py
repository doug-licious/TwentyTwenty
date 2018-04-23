from django.db import models
from desks.models import Desk

# Create your models here.


class DR_User(models.Model):
    PHONES = (
        ('IPC', 'IPC'),
        ('CISCO', 'CISCO')
    )
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    business_unit = models.CharField(max_length=5)
    phone = models.CharField(max_length=5, choices=PHONES)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    desk = models.ForeignKey(Desk, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.lastname
