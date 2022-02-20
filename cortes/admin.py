from django.contrib import admin
from .models import Corte

class Listando_cortes(admin.ModelAdmin):
    list_display = ('id', 'nome_corte', 'categoria', 'valor_corte')
    list_display_links = ('id', 'nome_corte')
    search_fields = ('nome_corte',)
    list_filter = ('categoria',)

# Register your models here.
admin.site.register(Corte, Listando_cortes)
