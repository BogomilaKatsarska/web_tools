from django.urls import path

from web_tools.web.views import index, EmployeesListView

urlpatterns = (
    path('', index, name='index'),
    path('employees/', EmployeesListView.as_view, name='employee list'),
)

from .signals import *