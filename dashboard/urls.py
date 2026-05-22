from django.urls import path
from .views import dashboard_api,dashboard_view, restart_container, start_container, stop_container, container_logs
from . import views
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
   
    path("api/", views.dashboard_api),
    #path("dashboard/api/", dashboard_api, name='dash_api'),

    # restart container
    path('restart/<str:name>/', restart_container, name='restart'),

    # start container
    path('start/<str:name>/', start_container, name='start'),

    # stop container
    path('stop/<str:name>/', stop_container, name='stop'),
   
    # logs Viewer
    path('logs/<str:name>/', container_logs, name='container_logs'),
]
