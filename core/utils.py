from decouple import config
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable, default=None):
    """Get environment variable by name.

    Raise error when environment variable is missing and default value is not set.

    Arguments:
        env_variable: variable name
        default: default value
    Returns:
        Value taken from environment variable or default value
    """

    try:
        return config(env_variable)
    except KeyError:
        if default is not None:
            return default
        else:
            raise ImproperlyConfigured(f"Set the {env_variable} environment variable")
