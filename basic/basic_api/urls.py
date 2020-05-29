from rest_framework import routers
from .api import ContactInfoViewSet


router = routers.DefaultRouter()
router.register('api/contactsInfo', ContactInfoViewSet, 'contactInfo')

urlpatterns = router.urls
