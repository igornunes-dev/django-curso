from django.test import TestCase
from core.form import ContatoForm


class ContatoFormTestCase(TestCase):

  def setUp(self):
    self.nome = 'Igor Nunes'
    self.email = 'igornunes@gmail.com'
    self.assunto = 'qualquer coisa'
    self.mensagem = 'uma mensagem qualquer'

    self.dados = {
      'nome': self.nome,
      'email': self.email,
      'assunto': self.assunto,
      'mensagem': self.mensagem
    }

    self.form = ContatoForm(data=self.dados) #ContatoForm(request.POST)

  def test_send_mail(self):
    form1 = ContatoForm(data=self.dados)
    form1.is_valid()
    res1 = form1.send_mail()

    form2 = self.form
    form2.is_valid()
    res2 = form2.send_mail()

    self.assertEqual(res1, res2)