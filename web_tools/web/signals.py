from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from web_tools.web.models import Employee

UserModel = get_user_model()

@receiver(signals.post_save, sender=Employee)
def handle_employee_create(*args, **kwargs):
    print(args)
    print(kwargs)


@receiver(signals.post_save, sender=UserModel)
def create_employee_on_user_create(instance, created,  *args, **kwargs):
    if not created:
        return

    Employee.objects.create(
        user_id=instance.pk,
    )


@receiver(signals.post_save, sender=UserModel)
def send_register_email_on_create(instance, created, *args, **kwargs):
    if not created:
        return

    Employee.objects.create(
        user_id=instance.pk,
    )
    pass