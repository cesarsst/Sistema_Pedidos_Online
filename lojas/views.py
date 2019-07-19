from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Lojas, Cardapio
from .forms import ComentarioLoja
# Create your views here.
def index_lojas(request):

    lojas = Lojas.objects.all()

    data = {
        'lojas': lojas
    }

    template_name = 'lojas/index_lojas.html'
    return render(request, template_name, data)


def details(request, slug):

    loja = Lojas.objects.all().filter(slug=slug)

    cad = loja[0].cardapio.all()

    data = {
        'loja': slug,
        'cardapios': cad,
    }

    template_name='lojas/details.html'

    return render(request, template_name, data)
