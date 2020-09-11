from django.contrib import admin
from django.urls import path
from taskapp import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_list/',views.task_list,name='task_list'),
    path('task_detail/<int:task_pk>',views.task_detail,name='task_detail'),
    path('task_create/',views.task_create,name='task_create'),
    path('task_update/<int:task_pk>',views.task_update,name='task_update'),
    path('task_delete/<int:task_pk>',views.task_delete,name='task_delete'),
    path('',TemplateView.as_view(template_name='index.html')),
]
