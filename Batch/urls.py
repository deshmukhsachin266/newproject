from django.urls import path

from . import views

urlpatterns=[
    path('sub/',views.SubjectVW,name='sub'),
    path('trainer/',views.TrainerVW,name='trainer'),
    path('profile/',views.TrainerDisplay,name='profile'),
    path('batchVW/',views.BatchVW,name='batchVW'),
    path('batchdisplay/',views.BatchDisplay,name='batchdisplay'),
    path('trainerupdate/<pk>/',views.TrainerUP,name='trainerupdate'),
    path('home/',views.Home,name='home'),
]