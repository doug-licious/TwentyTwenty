from import_export import resources
from .models import DR_User


class DR_UserResource(resources.ModelResource):
    class Meta:
        model = DR_User
