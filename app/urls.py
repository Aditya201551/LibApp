from django.urls import path
from app import views

app_name="app"
urlpatterns=[
    path('user_login/',views.user_login,name="user_login"),
    path('register/',views.register,name="register"),
    path('preference/', views.preference,name="preference"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('sites/',views.sites, name="sites"),
]
