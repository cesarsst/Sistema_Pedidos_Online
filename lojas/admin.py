from django.contrib import admin
from .models import Lojas, Cardapio, Pedido
# Register your models here.
class LojasAdmin(admin.ModelAdmin):

    #adiciona visualização rapida
    list_display = ['id', 'nome', 'slug', 'categoria', 'create_at']

    #Serve para buscar no admin pela caixa de busca
    search_fields = ['nome', 'slug']

    #Para criar o atalho automatico
    prepopulated_fields = {'slug':('nome',)}

class CardapioAdmin(admin.ModelAdmin):

    #adiciona visualização rapida
    list_display = ['nome', 'about', 'price', 'categoria']

    #Serve para buscar no admin pela caixa de busca
    search_fields = ['nome', 'categoria']

class PedidoAdmin(admin.ModelAdmin):

    #adiciona visualização rapida
    list_display = ['id_pedido', 'id_user', 'id_prato', 'id_loja']

    #Serve para buscar no admin pela caixa de busca
    search_fields = ['id_user', 'id_loja']


# Register your models here.
admin.site.register(Lojas, LojasAdmin)
admin.site.register(Cardapio, CardapioAdmin)
admin.site.register(Pedido, PedidoAdmin)
