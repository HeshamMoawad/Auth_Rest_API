from django.urls import path ,include
from .views import *

urlpatterns = [
    # path('login/',tasks_login),
    path('',tasks_login,name='login'),
    path('logout/',tasks_logout,name='logout'),
    path('tasks-list/',TasksListAPI.as_view(),name='tasks-list') ,
    path('task/<str:agentName>',analtics,name='analtics') ,
    path('more-info/<int:id>',task_info,name='task-info') ,
    path('add-note/',add_note,name='add_note')
] 


