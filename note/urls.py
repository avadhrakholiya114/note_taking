from django.urls import path
from . import views

urlpatterns = [

    path('notes/',views.list,name='notelist' ),

    path('notes/new', views.create_note, name='create_note'),
    path('notes/<id>', views.detail, name='detail'),


]