from django.urls import include, path

from rest_framework import routers

from mySiteApp.views import GemaLevelsViewSet

router = routers.DefaultRouter()
router.register(r'', GemaLevelsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]