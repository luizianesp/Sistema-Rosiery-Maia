from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        """
        Importa o módulo de sinais para garantir que os receivers de sinal sejam registrados.
        """
        import core.signals