from django.urls import path
from . import views

urlpatterns = [

    path('notes/',views.list,name='notelist' ),
    path('notes/<id>',views.detail )


]