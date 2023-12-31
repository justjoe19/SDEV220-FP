"""
URL configuration for finalproject project.

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
from timeclock.views import clock_in_out,employee_view,fire,pto_requests,submit_pto_request
from django.views.generic.base import RedirectView

admin.site.site_header = "Acme, Inc."
admin.site.site_title = "Acme, Inc."


urlpatterns = [
    path('', clock_in_out, name='home'),
    path('admin/', admin.site.urls),
    path('redirect/', RedirectView.as_view(pattern_name='home', permanent=False)),
    path("employeeView/",employee_view,name="employee_view"),
    path("fire/",fire,name="fire"),
    path("pto_requests/",pto_requests,name="pto_requests"),
    path("submit_pto_request/",submit_pto_request,name="submit_pto_request")
]

