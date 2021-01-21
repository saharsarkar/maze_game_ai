from django.urls import path

from core.views import bfs_view

urlpatterns = [
    path('bfs/', bfs_view),
]
