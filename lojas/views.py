from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Lojas, Cardapio, CustomUser, Pedido, Comanda
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
    p = Pedido.objects.all().filter(id_pedido=id, id_user=request.user.id, id_loja=id_loja[0], is_active=False)

    p.delete()

    return redirect('details', slug=page)

def del_carrinho(request, page):

    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_user=request.user.id, id_loja=id_loja[0], is_active=False)

    p.delete()

    return redirect('details', slug=page)

def finaliar_compra(request, page):

    #Procura por pedidos com base na loja_slug, user,
    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_user=request.user.id, id_loja=id_loja[0], is_active=False)


    sum = 0
    var = 0
    for items in p:

        comanda = Comanda()
        comanda.id_pedido = items
        comanda.total_comanda = items.id_prato.price
        comanda.id_user = request.user
        comanda.id_loja = id_loja[0]
        comanda.save()

        if var == 0:
            # var auxilia
            var = comanda.id
            comanda.id_comanda = var
            comanda.save()

        else:
            comanda.id_comanda = var
            comanda.save()

        sum += comanda.id_pedido.id_prato.price

    data = {
        'pedidos': p,
        'total': sum,
        'page': page,
    }

    template_name = 'lojas/finalizar_compra.html'
    return render(request, template_name, data)

def confirma_compra(request, page):

    # Procura por pedidos com base na loja_slug, user,
    id_loja = Lojas.objects.all().filter(slug=page)
    p = Pedido.objects.all().filter(id_user=request.user.id, id_loja=id_loja[0], is_active=False)

    for items in p:
        items.is_active = True
        items.save()

    return redirect('acompanhar_pedidos')


def acompanhar_pedidos(request):
    user = request.user

    # Seleciona comandas pertencentes ao usuario
    comandas = Comanda.objects.all().filter(id_user=user.id)

    # Armazena as IDs (sem repetição) das comandas em 'list'
    list = []
    atual = 0
    for comanda in comandas:
       if atual == 0:
         atual = comanda.id_comanda
         list.append(atual)
       else:
           if comanda.id_comanda == atual:
                pass
           else:
               atual = comanda.id_comanda
               list.append(atual)


    context = {}
    pedidos = []
    aux = []

    # Para cada Id de comanda em list, armazena os respectivos dados dos pedidos em 'Aux'
    for item in list:
        pedidos.clear()
        context['id'] = item
        sum = 0
        for comanda in comandas:
            if comanda.id_comanda == item:
                pedidos.append(comanda)
                sum += comanda.total_comanda
                status = comanda.status
                user_view = comanda.user_view
        context['sum'] = sum
        context['status'] = status
        context['user_view'] = user_view
        context['pedidos'] = pedidos.copy()
        aux.append(context.copy())

    data = {
        'data': aux
    }

    template_name = 'lojas/acompanhar_pedidos.html'

    return render(request, template_name, data)

def desativa_pedidos(request, id):

    comandas = Comanda.objects.all().filter(id_comanda=id)

    for items in comandas:
        items.user_view = 1
        items.save()

    return redirect('acompanhar_pedidos')