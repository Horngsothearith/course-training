from django.urls import path

from training import views

urlpatterns = [
    path('create_trainee', views.create_trainee, name='create_trainee'),
    path('create_course', views.create_course, name='create_course'),
    path('course_register', views.course_register, name='course_register'),
    path('create_certification', views.create_certification, name='create_certification'),
    path('create_attendance', views.create_attendance, name='create_attendance'),
    # get
    # all
    path('get_all_trainee', views.get_all_trainee, name='get_all_trainee'),
    path('get_all_course_register', views.get_all_course_register, name='get_all_course_register'),
    path('get_all_course', views.get_all_course, name='get_all_course'),
    path('get_all_certification', views.get_all_certification, name='get_all_certification'),
    path('get_all_attendance', views.get_all_attendance, name='get_all_attendance'),
    # by id
    path('get_trainee_by_id', views.get_trainee_by_id, name='get_trainee_by_id'),
    path('get_course_by_id', views.get_course_by_id, name='get_course_by_id'),
    path('get_certification_by_id', views.get_certification_by_id, name='get_certification_by_id'),
]
