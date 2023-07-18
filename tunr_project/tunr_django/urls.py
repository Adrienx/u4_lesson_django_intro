"""
URL configuration for tunr_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include

# On the first line, we are adding an import - include - so that we can include other url files in our main one. We are doing this in order to make our app more modular. These "mini apps" in Django are supposed to plug into another parent app if needed, and modularity makes this possible.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tunr.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
