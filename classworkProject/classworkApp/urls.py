from django.urls import path

from . import views
# send paths
urlpatterns = [
    path('', views.index, name='index'),
]