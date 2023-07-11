from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    age = models.PositiveIntegerField()
