from django.urls import path

from core.views import bfs_view, ids_view

urlpatterns = [
    path('bfs/', bfs_view),
    path('ids/', ids_view),
]
