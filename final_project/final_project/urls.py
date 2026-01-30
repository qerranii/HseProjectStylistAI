"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from final_project_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('log_in/', log_in_page, name='log_in'),
    path('sign_up/', sign_up_page, name='sign_up'),
    path('profile/', profile_page, name='profile'),
    path('profile_edit/', profile_edit_page, name='profile_edit'),
    path('gallery_liked/', gallery_liked_page, name='gallery_liked'),
    path('top_outfits/', top_outfits_page, name='top_outfits'),
    path('scrolling/', scrolling_page, name='scrolling'),
    path('about/', about_page, name='about'),
    path('terms/', terms_page, name='terms'),
]
