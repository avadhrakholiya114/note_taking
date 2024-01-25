from django.urls import path
from . import views

urlpatterns = [

    path('notes/', views.list, name='notelist'),

    path('notes/new', views.create_note, name='create_note'),
    path('notes/<id>', views.detail, name='detail'),
    path('notes/<id>/update/', views.update_note, name='update_note'),
    path('notes/<id>/delete/', views.delete_note, name='delete_note'),
    path('register/', views.regi, name='register'),
    path('login/', views.login_form, name='custom_login'),
    path('Logout_user/', views.Logout_user,name='logout_user')

]
