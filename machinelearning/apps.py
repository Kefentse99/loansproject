from django.apps import AppConfig


class MachinelearningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'machinelearning'
    
    def ready(self):
    	import machinelearning.signals
