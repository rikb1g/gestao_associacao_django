from django.apps import AppConfig


class EscolasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.escolas'

    def ready(self):
        import apps.escolas.signals