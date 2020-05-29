from rest_framework import viewsets, permissions
from basic_api.models import ContactInfo
from .serializers import ContactSerializer

# contact info viewset


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer
