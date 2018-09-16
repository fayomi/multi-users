from django.urls import path
from . import views

app_name='testing'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('accounts/trainer',views.trainerRegister,name='trainer_signup'),
    path('trainers',views.TrainerListView.as_view(),name='list'),

]
