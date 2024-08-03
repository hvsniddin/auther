from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import login, CustomTokenObtainPairView, ott, verify


urlpatterns = [
    path('', login, name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('ott/', ott, name='ott'),
    path('verify/', verify, name='verify'),
]
