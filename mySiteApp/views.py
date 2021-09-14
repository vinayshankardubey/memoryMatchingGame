# Create your views here.
from rest_framework import viewsets

from mySiteApp.serializers import GemaLevelsSerializer
from mySiteApp.models import GemaLevels


class GemaLevelsViewSet(viewsets.ModelViewSet):
   queryset = GemaLevels.objects.all()
   serializer_class = GemaLevelsSerializer
