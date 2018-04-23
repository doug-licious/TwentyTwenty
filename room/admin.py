from django.contrib import admin

# Register your models here.

# from .resources import DR_UserResource
from .models import Room
from .models import Computer
from .models import DRUser
from .models import Software
from .models import Desk

admin.site.register(Room)
admin.site.register(Computer)
admin.site.register(DRUser)
admin.site.register(Software)
admin.site.register(Desk)
