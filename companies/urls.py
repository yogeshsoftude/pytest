from rest_framework import routers
from .views import CompanyViewSet , send_company_mail
from django.urls import path

compnies_router = routers.DefaultRouter()
compnies_router.register("companies", viewset=CompanyViewSet, basename="companies")
