from django.urls import path
from . import views
'''Define URL Patterns for the Django Project'''
urlpatterns = [
    path('',views.login,name="login"),                                   # Renders the login page
    path('student/',views.student_home,name="home_s"),                   # Renders the student's homepage
    path('chef/',views.chef_home,name="home_c"),                         # Renders the chef's homepage
    path('chef/selection', views.chef_select, name="home_c_s"),          # Handles chef's menu selection
    path('logout',views.logout, name="logout"),                          # Handles user logout
    path('chef/<int:pk>/deletes',views.delete, name="deletes"),          # Deletes a menu object
    path('student/<int:pk>/attending',views.attending,name="attending"), # Handles attendance for a menu item
]