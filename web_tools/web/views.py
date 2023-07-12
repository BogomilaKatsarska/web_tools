import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from web_tools.web.models import Employee

CLICKS_COUNT_SESSION_KEY = 'CLICKS_COUNT_SESSION_KEY'
LATEST_VALUE_SESSION_KEY = 'LATEST_VALUE_SESSION_KEY'


def very_slow_operation():
    return random.randint(1, 1024)


@cache_page(1 * 60)
def index(request):
    Employee.objects.create(
        first_name='Bogomila',
        last_name='Katsarska',
        age=28,
    )
    clicks_count = request.session.get('CLICKS_COUNT_SESSION_KEY', 0) + 1
    request.session[CLICKS_COUNT_SESSION_KEY] = clicks_count
    value = very_slow_operation()
    latest_values = request.session.get(LATEST_VALUE_SESSION_KEY, [])
    latest_values = [value] + latest_values
    request.session[LATEST_VALUE_SESSION_KEY] = latest_values[:3]
    return HttpResponse(f'Value is {value}, clicks: {clicks_count}, latest values:{", ".join(str(x) for x in latest_values)}')


class EmployeesListView(ListView):
    model = Employee
    template_name = 'employees/list.html'
    #paginate_by = 3

    #in order to make it dynamic use below:
    def get_paginate_by(self, queryset):
        return random.randint(3,7)