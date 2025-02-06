from django.contrib import admin
from .models import Cargo, Service, Funcionario, Features1
# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
  list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
  list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Features1)
class FeaturesAdmin(admin.ModelAdmin):
  list_display = ('nome', 'icone', 'ativo', 'modificado')
