from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import CompanySerializers
from .models import Companies

class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Companies.objects.all().order_by('-last_update')
    pagination_class = PageNumberPagination
