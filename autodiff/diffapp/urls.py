from django.urls import path
from . import views
app_name = 'diff'

urlpatterns = [
    path('', views.get_version),
    path('display/', views.display, name='display')
]