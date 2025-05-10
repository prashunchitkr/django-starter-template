from configurations.values import ListValue
from corsheaders.defaults import default_headers, default_methods


class CorsSettings:

    ALLOWED_HOSTS = ListValue()

    CORS_ALLOWED_ORIGINS = ListValue()

    CSRF_TRUSTED_ORIGINS = ListValue()

    CORS_ALLOW_CREDENTIALS = True

    CORS_ALLOW_METHODS = (*default_methods,)

    CORS_ALLOW_HEADERS = (*default_headers,)

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
