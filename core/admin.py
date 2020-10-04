from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import location
# Register your models here.

class locationAdmin( LeafletGeoAdmin):
  
    settings_overrides =  {
        'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 8,
        'MIN_ZOOM': 5,  
        'MAX_ZOOM': 24,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
 
    list_display = ('latlng',)
  

admin.site.register(location,locationAdmin)