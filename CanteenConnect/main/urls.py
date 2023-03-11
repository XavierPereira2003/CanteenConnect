from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('student/',views.student_home,name="home_s"),
    path('chef/',views.chef_home,name="home_c"),
    path('chef/selection', views.chef_select, name="home_c_s"),
    path('logout',views.logout, name="logout"),

    path('student/<int:pk>/attending',views.attending,name="Attending")
]