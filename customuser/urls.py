from django.urls import path

from customuser.views import register_view , login_view,get_iterations_view

app_name = 'users'

urlpatterns = [
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('get_iterations/', get_iterations_view, name='get_iterations'),
]
