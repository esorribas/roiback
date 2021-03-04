
from django.contrib import admin

from roiback import models


admin.site.register(models.Hotel)
admin.site.register(models.Room)
admin.site.register(models.Rate)
admin.site.register(models.Inventory)

admin.site.site_title = 'Roiback - Consola de administración'
admin.site.site_header = 'Roiback - Consola de administración'
admin.site.index_title = 'Roiback - Consola de administración'
