from django.db.models import signals


@signals.post_save()
def handle_employee_create(*args, **kwargs):
    print(args)
    print(kwargs)