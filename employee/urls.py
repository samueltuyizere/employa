from rest_framework import routers
from django.conf.urls import include, url
from .views import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]