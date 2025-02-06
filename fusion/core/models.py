from django.db import models
import uuid
from stdimage.models import StdImageField
# Create your models here.


def get_file_path(_instance, filename):
  ext = filename.split(".")[-1]
  filename = f'{uuid.uuid4()}.{ext}'
  return filename

class Base(models.Model):
  criados = models.DateField("Criação", auto_now_add=True)
  modificado = models.DateField("Atualização", auto_now=True)
  ativo = models.BooleanField("Ativo", default=True)

  class Meta:
    abstract = True

class Service(Base):
  icone_choice = [
    ('lni-cog', 'Engrenagem'),
    ('lni-start-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
]
  servico = models.CharField("Service", max_length=100)
  descricao = models.TextField("Descrição", max_length=200)
  icone = models.CharField("Icone", max_length=12, choices=icone_choice)

  class Meta:
    verbose_name = "Service"
    verbose_name_plural = "Services"

  def __str__(self):
    return self.servico
  
class Cargo(Base):
  cargo = models.CharField("Cargo", max_length=100)

  class Meta:
    verbose_name = 'Cargo'
    verbose_name_plural = "Cargos"

  def __str__(self):
    return self.cargo

class Funcionario(Base):
  nome = models.CharField("Nome", max_length=100)
  cargo = models.ForeignKey('core.Cargo', verbose_name="Cargo", on_delete=models.CASCADE)
  bio = models.TextField("Bio", max_length=100)
  imagem = StdImageField("Imagem", upload_to=get_file_path, variations={"thumb": {"width": 480, "height": 480}})
  facebook = models.CharField("Facebook", max_length=100, default='#')
  twitter = models.CharField("Twitter", max_length=100, default='#')
  instagram = models.CharField("Instagram", max_length=100, default='#')

  class Meta:
    verbose_name = 'Functionário'
    verbose_name_plural = 'Funcionários'
  
  def __str__(self):
    return self.nome
  

class Features1(Base):
  icone_choice = [
    ('lni-cog', 'Engrenagem'),
    ('lni-start-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
]
  nome = models.CharField("Nome", max_length=100)
  descricao = models.CharField("Descrição", max_length=200)
  icone = models.CharField("Icone", max_length=12, choices=icone_choice)

  class Meta:
    verbose_name = "Feature1"
    verbose_name_plural = "Features1"

  def __str__(self):
    return self.nome

