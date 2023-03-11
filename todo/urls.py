from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>/', views.todo_complete, name='todo-complete')
]
