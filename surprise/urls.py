from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('home/', views.home, name='home'),
    path('beginning/', views.beginning, name='beginning'),
    path('memories/', views.memories, name='memories'),
    path('letter/', views.letter, name='letter'),
    path('cake/', views.cake, name='cake'),
    path('final/', views.final, name='final'),

    path('logout/', views.logout_view, name='logout'),
]