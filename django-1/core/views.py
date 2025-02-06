from django.shortcuts import render

# Create your views here.
# Função que são chamadas nas nossas rotas

def index(request):
  return render(request, 'index.html')

def contato(request):
  return render(request, 'contato.html')
