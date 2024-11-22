from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("logout", views.logout_views),
    path("task_list", views.task_list, name='task-list'),
    path('task_list/create/', views.task_create, name='task-create'),
    path("task_list/update/<int:pk>/",views.task_update, name="task-update"),
    path("task_list/delete/<int:pk>/", views.task_delete, name="task-delete"),

]
