from django.urls import path, include
from rest_framework_nested import routers
from .views import SchoolViewSet, StudentViewSet

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)
schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(schools_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
