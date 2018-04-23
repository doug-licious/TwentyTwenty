from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('import/', views.import_desk, name='import_desk'),
	path('<int:desk_id>/', views.detail, name='detail')
]