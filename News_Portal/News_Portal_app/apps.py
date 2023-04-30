from django.apps import AppConfig
import redis

red = redis.Redis(
    host='redis-16727.c267.us-east-1-4.ec2.cloud.redislabs.com',
    port=16727,
    password='MFHVrzZfBA6yvYDOUQI8Uy3JkFffmdS6'
)


class NewsPortalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News_Portal_app'

    def ready(self):
        import News_Portal_app.signals
