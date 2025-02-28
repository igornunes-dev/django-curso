from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Service, Funcionario, Features1
from .form import ContatoForm

class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContatoForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['service'] = Service.objects.all().order_by('?').all()
    context['funcionario'] = Funcionario.objects.all()
    context['features1'] = Features1.objects.all().order_by('?').all()[:3]
    context['features2'] = Features1.objects.all().order_by('?').all()[3:6]
    return context
  
  def form_valid(self, form, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'Email enviado com sucesso')
    return super(IndexView, self).form_valid(form, *args, **kwargs)
  
  def form_invalid(self, form, *args, **kwargs):
    messages.error(self.request, 'Erro ao enviar email')
    return super(IndexView, self).form_invalid(form, *args, **kwargs)



