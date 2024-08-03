import secrets
from django.core.cache import cache


def generate_ott():
    """
    Generates a URL-safe one-time-token.
    """
    return secrets.token_urlsafe(48)


def set_ott(ott, token_pair):
    """
    Saves the given OTT with the access token in the cache for 2 minutes.
    """
    cache.set(ott, token_pair, timeout=120)
