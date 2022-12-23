from django.conf.urls import urls
from EmployeeApp import views

urlpatterns = [
    urls(r'^department$', views.departmentApi),
    url(r'^department/[0-9]+)$')
]