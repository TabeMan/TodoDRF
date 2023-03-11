from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    path('', views.TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', views.TodoRetrieveUpdateDestroyView.as_view(),
         name='todo-retrieve-update-destroy'),
    path('profile/<int:pk>/', views.ProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
