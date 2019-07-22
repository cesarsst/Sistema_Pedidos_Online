from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Lojas, Cardapio, CustomUser, Pedido
from .forms import ComentarioLoja
from django.shortcuts import redirect


# Create your views here.
def index_lojas(request):

    lojas = Lojas.objects.all()

    data = {
        'lojas': lojas
    }

    template_name = 'lojas/index_lojas.html'
    return render(request, template_name, data)


def details(request, slug):

    #Encontrando cardapio da loja
    loja = Lojas.objects.all().filter(slug=slug)
    cad = loja[0].cardapio.all()

    #Encontrando pedidos
    pedidos = Pedido.objects.all().filter(id_user=request.user.id, id_loja=loja[0].id, is_active=False)

    sum = 0
    for pedido in pedidos:
        sum = sum + pedido.id_prato.price

    data = {
        'page': slug,
        'cardapios': cad,
        'pedidos': pedidos,
        'total': sum
    }

    template_name = 'lojas/details.html'

    return render(request, template_name, data)


def pedido(request, id, page):

    u = CustomUser.objects.all().filter(id=request.user.id)
    p = Cardapio.objects.all().filter(id=id)
    l = Lojas.objects.all().filter(slug=page)

    new = Pedido()
    new.id_user = u[0]
    new.id_prato = p[0]
    new.id_loja = l[0]
    new.save()

    return redirect('details', slug=page)

def del_pedido(request, id, page):

    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_pedido=id, id_user=request.user.id, id_loja=id_loja[0])

    p.delete()

    return redirect('details', slug=page)

def del_carrinho(request, page):

    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_user=request.user.id, id_loja=id_loja[0])

    p.delete()

    return redirect('details', slug=page)

def finaliar_compra(request, page):

    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_user=request.user.id, id_loja=id_loja[0])

    for items in p:
        items.is_active = True
        items.save()


    data = {
        'pedidos': p,
    }

    template_name = 'lojas/finalizar_compra.html'
    return render(request, template_name, data)