
from django.contrib.gis.db import models

# Create your models here.

class location (models.Model):
   
    latlng = models.PointField(null=True,unique=True)
    
    
   
    class Meta:
        verbose_name_plural = "location"
     