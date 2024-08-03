from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .utils import generate_ott, set_ott


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        super().validate(attrs)
        refresh = self.get_token(self.user)
        ott=generate_ott()
        set_ott(ott, {'access': str(refresh.access_token), 'refresh': str(refresh)})
        return {'ott': ott}
