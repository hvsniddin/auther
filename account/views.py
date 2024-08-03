from django.shortcuts import render
from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


def login(r):
    return render(r, 'login.html')


@api_view(['POST'])
def ott(r):
    """
    Uses ott to return a pair of tokens.
    """
    ott = r.data.get('ott')
    if not ott: return Response(data=None, status=status.HTTP_400_BAD_REQUEST)
    token = cache.get(ott)
    cache.delete(ott)
    return Response(data=token, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify(r):
    """
    Verifies the token and matches the dashboard ids.
    """
    dashboard_id = r.data.get('dashboard_id')
    return Response(data={'ok':dashboard_id==r.user.dashboard_id})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
