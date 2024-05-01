from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import CompanySerializers
from .models import Companies
from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.core.mail import send_mail

from rest_framework.response import Response
from django.conf import settings


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Companies.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination



@api_view(http_method_names=['POST'])
def send_company_mail(request:Request) -> Response: 


    # Example usage of send_mail
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.DEFAULT_EMAIL_FROM,
        ['yogesh.baraskar@softude.com'],
        fail_silently=False,
    )
    return Response({'status':'success','Info':'Email sent successfully'})



def fibonacci_naive(n: int) -> None:
    if n==0 or n==1:
        return n
    return fibonacci_naive(n-2) + fibonacci_naive(n-1)
