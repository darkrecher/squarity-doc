"""squarity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# https://stackoverflow.com/questions/15706489/redirect-to-named-url-pattern-directly-from-urls-py-in-django
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', lambda request: redirect('/index.html', permanent=False)),
    # path('', lambda request: redirect('/index.html', permanent=False)),
]
