from datetime import timedelta

from configurations.values import SecretValue, Value


class JWTSettings:

    SIGNING_KEY = SecretValue()

    JWT_ALGORITHM = Value(default="HS256")

    SIMPLE_JWT = {
        "USER_ID_CLAIM": "user_id",
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "ROTATE_REFRESH_TOKENS": True,
        "BLACKLIST_AFTER_ROTATION": True,
        "UPDATE_LAST_LOGIN": True,
        "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
        "TOKEN_OBTAIN_SERIALIZER": "_auth.serializers.TokenSerializer",
    }
