from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from _auth.models import User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token["email"] = user.email

        return token
