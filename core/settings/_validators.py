class ValidatorsSettings:

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa 501
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa 501
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa 501
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa 501
        },
    ]
