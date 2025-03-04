from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', '_author')
  exclude = ['author']

  def _author(self, instance):
    #instance = POST
    #author que possui o meto do get_full_name()
    return f'{instance.author.get_full_name()}'
  
  #mostra novamente os autor que esta logado
  def get_queryset(self, request):
    gs = super().get_queryset(request)
    return gs.filter(author=request.user)
  
  def save_model(self, request, obj, form, change):
    # O obj que é o post do author ele recebe o dados do usuario que esta logado
    obj.author = request.user
    super().save_model(request, obj, form, change)
