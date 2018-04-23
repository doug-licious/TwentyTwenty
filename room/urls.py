from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import_users/', views.import_users, name='import_users'),
    path('import_desks/', views.import_desks, name='import_desks'),
    path('import_computers/', views.import_computers, name='import_computers'),
    path('import_software/', views.import_software, name='import_software'),
    path('software', views.software, name='software'),
    path('software2', views.software2, name='software2'),
    path('computers', views.computers, name='computers'),
    path('graph', views.graph, name='graph'),
    path('desk/<int:desk_number>', views.desk, name='desk'),
    path('computer/<str:hostname>', views.computer, name='computer')
    # path('query/', views.query_user, name='query_user'),
    # path('<int:user_id>/', views.detail, name='detail')
]
