from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='todo-home'),
    path('about', views.about_page, name='todo-about'),
    path('add-todo', views.add_todo, name='todo-add-todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='update-todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
