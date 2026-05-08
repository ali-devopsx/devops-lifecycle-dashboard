"""
Django App Configuration for Identity Portfolio
This module configures the 'identity' app and runs default data population on app startup.
"""

from django.apps import AppConfig


class IdentityConfig(AppConfig):
    """
    Configuration for the identity app.
    This runs when Django starts and ensures default data is populated.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'identity'
    verbose_name = 'Digital Identity Portfolio'

    def ready(self):
        """
        This method runs when the Django app is ready.
        It's used to populate default data into the database if it doesn't already exist.
        This ensures the portfolio always has data to display.
        """
        from .utils import populate_default_data
        try:
            # Attempt to populate default data
            # Wrapped in try-except because during initial migration, the database tables may not exist yet
            populate_default_data()
        except Exception:
            # Silently fail if database tables don't exist (during migrations)
            # This is normal and expected on first run before migrations are applied
            pass
