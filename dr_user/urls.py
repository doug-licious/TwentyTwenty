from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.import_user, name='import_user'),
    path('query/', views.query_user, name='query_user'),
    path('<int:user_id>/', views.detail, name='detail')
]
