from import_export import resources, fields
from .models import DRUser, Desk
from import_export.widgets import ManyToManyWidget


class DRUserResource(resources.ModelResource):
    #desk = fields.Field(widget=ManyToManyWidget(Desk))
    import_id_field = ('UserName',)

    class Meta:
        model = DRUser


class DeskResource(resources.ModelResource):
    import_id_field = ['desk_number']

    class Meta:
        model = Desk
