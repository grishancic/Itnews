from.import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.home,name="home"),
    path('applications', views.appl,name="applications"),
    path('contacts', views.cont,name="contacts"),
    path('portfolio', views.port,name="portfolio")

]