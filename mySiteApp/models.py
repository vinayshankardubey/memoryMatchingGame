from django.db import models
  

class GemaLevels(models.Model):  
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

      
