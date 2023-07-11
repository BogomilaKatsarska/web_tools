from django.urls import path

from web_tools.web.views import index

urlpatterns = (
    path('', index, name='index'),
)