import os
from django.apps import AppConfig
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        logger.error(f"ADMIN_USERNAME={username}")
        logger.error("READY() CALLED")

        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                logger.error("ADMIN CREATED")
            else:
                logger.error("ADMIN ALREADY EXISTS")
