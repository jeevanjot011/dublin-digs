"""
URL configuration for listings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.browse_listings, name='browse_listings'),
    path('add/', views.add_listing, name='add_listing'),
    path('<int:id>/edit/', views.edit_listing, name='edit_listing'),
    path('<int:id>/delete/', views.delete_listing, name='delete_listing'),
    path('<int:id>/', views.view_listing, name='view_listing'),
     path('set-preferred-area/', views.set_preferred_area, name='set_preferred_area'),
]
