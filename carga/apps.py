from django.apps import AppConfig


class CargaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carga'
  
class CargaConfig(AppConfig):
    name = 'carga'
  
    def ready(self):
        import carga.signals