from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

  def setUp(self):
    self.dados = {
      'nome': 'Igor Nunes',
      'email': 'igornunes@gmail.com',
      'assunto': 'Meu assunto',
      'mensagem': 'Minha mensagem',
    }
    self.cliente = Client()

  def test_form_valid(self):
    request = self.cliente.post(reverse_lazy('index'), data=self.dados)
    self.assertEqual(request.status_code, 302)

  def test_form_invalid(self):
    dados = {
      'nome': 'IGor Nunes',
    }
    request = self.cliente.post(reverse_lazy('index'), data=dados)
    self.assertEqual(request.status_code, 200)