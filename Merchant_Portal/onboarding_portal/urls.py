from django.urls import path
from .views import *
#................................................................

urlpatterns = [
    path('vendore_onboarding',vendor_onboarding,name='vendor_onboarding'),
]