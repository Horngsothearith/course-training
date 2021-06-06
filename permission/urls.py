from django.urls import path

from permission import views

urlpatterns = [
    path('create_group', views.create_group, name='create_group'),
    path('create_role', views.create_role, name='create_role'),
    # get
    path('get_all_group', views.get_all_group, name='get_all_group'),
    path('get_all_role', views.get_all_role, name='get_all_role'),
]
