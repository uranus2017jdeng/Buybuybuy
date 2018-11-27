from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from super import views

app_name='supper'
urlpatterns = [
    url(r'^index$', views.index, name='index'),
]