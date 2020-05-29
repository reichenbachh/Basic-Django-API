from rest_framework import serializers
from basic_api.models import ContactInfo

# contact info serializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
