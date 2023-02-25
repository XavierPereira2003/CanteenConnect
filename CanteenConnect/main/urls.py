from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('student/',views.student_home,name="home_s"),
    path('chef/',views.chef_home,name="home_c"),
]