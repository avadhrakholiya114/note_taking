from django.urls import path
from . import views

urlpatterns = [

    path('notes/',views.list ),
    path('notes/<id>',views.detail )


]