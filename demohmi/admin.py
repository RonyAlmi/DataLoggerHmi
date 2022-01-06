from django.contrib import admin
from.models import valores

class ValoresAdmin(admin.ModelAdmin):
    list_display = ('id','parametros', 'valor', 'descripcion')

admin.site.register(valores,ValoresAdmin)
