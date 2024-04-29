from rest_framework import serializers
from .models import Companies

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id','name','status', 'application_link','last_update','notes']
        
