from import_export import resources
from .models import Desk


class DeskResource(resources.ModelResource):
    class Meta:
        model = Desk
