from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    # main 문지기에게 알려주러가자.

    path('users/<int:pk>/', views.user_detail),

]
