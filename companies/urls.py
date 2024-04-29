from rest_framework import routers
from .views import CompanyViewSet

compnies_router = routers.DefaultRouter()
compnies_router.register("companies",viewset=CompanyViewSet,basename="companies")
