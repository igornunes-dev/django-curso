from django.contrib import admin
from .models import Chassi, Carro, Montadora
# Register your models here.

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
  list_display = ('numero',)



@admin.register(Carro)
class ChassiAdmin(admin.ModelAdmin):
  list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motorista')

  def get_motorista(self,obj):
    return  ', '.join([m.username for m in obj.motorista.all()])
  
  get_motorista.short_description = 'Motoristas'

@admin.register(Montadora)
class ChassiAdmin(admin.ModelAdmin):
  list_display = ('nome',)

