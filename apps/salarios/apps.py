from django.apps import AppConfig


class SalariosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.salarios"

    def ready(self):
        import apps.salarios.signals
