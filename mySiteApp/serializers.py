from rest_framework import serializers

from mySiteApp.models import GemaLevels

class GemaLevelsSerializer(serializers.ModelSerializer):
   class Meta:
       model = GemaLevels
       fields = ('name', 'classification', 'language')

