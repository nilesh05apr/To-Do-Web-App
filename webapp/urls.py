from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('complete',views.completed, name='completed'),
    path('incomplete',views.incompleted,name='incomplete'),
    path('update/<int:p_id>',views.mark_complete,name='mark_complete'),
    path('delete/<int:p_id>',views.delete_task,name='delete_task')
]
