from django.urls import path
from .views import dashboard_view, restart_container, start_container, stop_container, container_logs

urlpatterns = [
    path('', dashboard_view, name='dashboard'),

    # restart container
    path('restart/<str:name>/', restart_container, name='restart'),

    # start container
    path('start/<str:name>/', start_container, name='start'),

    # stop container
    path('stop/<str:name>/', stop_container, name='stop'),
   
    # logs Viewer
    path('logs/<str:name>/', container_logs, name='container_logs'),
]
