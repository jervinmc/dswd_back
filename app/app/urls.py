from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import GetUserView,Signup
from beneficiaries.views import BeneficiariesID
from sap.views import SAPID,SAPBarangay,Requests,CheckSAP
from donate.views import DonateID
from ps.views import PSID,CheckPS
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/cases/', include('cases.urls')),
    path('api/v1/beneficiaries/', include('beneficiaries.urls')),
    path('api/v1/donate/', include('donate.urls')),
    path('api/v1/sap/', include('sap.urls')),
    path('api/v1/barangay/', include('barangay.urls')),
    path('api/v1/location/', include('location.urls')),
    path('api/v1/ps/', include('ps.urls')),
    path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
    path('api/v1/bene/id/', BeneficiariesID.as_view(), name='get_user'),
    path('api/v1/sap_id/id/', SAPID.as_view(), name='get_user'),
    path('api/v1/barangaysap/', SAPBarangay.as_view(), name='get_user'),
    path('api/v1/donate_id/id/', DonateID.as_view(), name='get_user'),
    path('api/v1/ps_id/id/', PSID.as_view(), name='get_user'),
    path('api/v1/requests/', Requests.as_view(), name='get_user'),
    path('api/v1/check4ps/<str:user_id>/', CheckPS.as_view(), name='get_user'),
    path('api/v1/checkSAP/<str:user_id>/', CheckSAP.as_view(), name='get_user'),
    
    
]