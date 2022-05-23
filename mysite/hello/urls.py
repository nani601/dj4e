from django.urls import path

from . import views

app_name = "hello"


urlpatterns = [
    # ex: /hello/
    path('', views.index, name='index'),
]
