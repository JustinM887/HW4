from django.urls import path
from . import views

urlpatterns = [
    path('index', views.view_todos, name='index'),
    path('update/<str:id>', views.update_todo, name='update'),
    path('delete/<str:id>', views.delete_todo, name='delete'),
    path('complete_task/<str:id>', views.complete_task, name='complete_task')
]