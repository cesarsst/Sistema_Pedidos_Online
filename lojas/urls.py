from django.contrib import admin
from django.urls import path
from lojas.views import index_lojas, details, pedido, del_pedido, del_carrinho, finaliar_compra, confirma_compra, acompanhar_pedidos, desativa_pedidos
from . import views

urlpatterns = [
    path('', index_lojas, name='index_lojas'),
    path('<slug:slug>', details, name='details'),
    path('add/<int:id>/<slug:page>', pedido, name='pedido'),
    path('del/<int:id>/<slug:page>', del_pedido, name='del_pedido'),
    path('del/<slug:page>', del_carrinho, name='del_carrinho'),
    path('finalizar/<slug:page>', finaliar_compra, name='finalizar_compra'),
    path('confirma/<slug:page>', confirma_compra, name='confirma_compra'),
    path('acompanharPedido/', acompanhar_pedidos, name='acompanhar_pedidos'),
    path('desativaPedido/<int:id>', desativa_pedidos, name='desativa_pedidos')
]