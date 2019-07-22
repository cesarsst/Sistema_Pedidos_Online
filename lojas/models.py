from django.db import models
from users.models import CustomUser




class LojasManager(models.Manager):

    #Puxa todos os registros que tenham no Nome ou Slug = Query
    def get_queryset(self):
        return super().get_queryset().filter(slug='loja-teste')

class CardapioManager(models.Manager):

    #Puxa todos os registros que tenham no Nome ou Slug = Query
    def search(self, query):
        return Cardapio.objects.filter(models.Q(nome__icontains=query)
                                     | models.Q(slug__icontains=query))

class PedidoManager(models.Manager):

    #Puxa todos os registros que tenham no Nome ou Slug = Query
    def get_queryset(self):
        return super().get_queryset().filter(user='loja-teste')

# Create your models here.

class Lojas(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    about = models.TextField('Sobre', blank=True)
    create_at = models.DateTimeField('Data de adesão', auto_now_add=True)
    updated_at = models.DateTimeField('Atualiza em', auto_now=True)
    categoria = models.CharField('Categoria', max_length=100)                       #mudar depois
    image = models.ImageField(upload_to='media/images', verbose_name='Imagem',
                              null=True, blank=True)

    objects = models.Manager()
    objectsSearch = LojasManager()

    def __str__(self):
        return self.nome

    class Meta:

        #Define como irá aparecer em formularios e no admin
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

        # Ordena de forma alfabetica (para inverso colocar -)
        ordering = ['nome']

class Cardapio(models.Model):
    nome = models.CharField('Nome', max_length=100)
    about = models.TextField('Sobre', blank=True)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2, max_length=None)
    categoria = models.CharField('Categoria', max_length=100)
    image = models.ImageField(upload_to='media/images', verbose_name='Imagem',
                              null=True, blank=True)
    loja = models.ForeignKey(Lojas, on_delete=models.CASCADE, related_name='cardapio')

    objects = models.Manager()
    objectsSearch = CardapioManager()

    def __str__(self):
        return self.nome

    class Meta:
        # Define como irá aparecer em formularios e no admin
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapios'

        # Ordena de forma alfabetica (para inverso colocar -)
        ordering = ['nome']


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedido')
    id_prato = models.ForeignKey(Cardapio, on_delete=models.CASCADE, related_name='pedido')
    id_loja = models.ForeignKey(Lojas, on_delete=models.CASCADE, related_name='pedido')
    is_active = models.BooleanField(default=False)
    objects = models.Manager()


    class Meta:
        # Define como irá aparecer em formularios e no admin
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

        # Ordena de forma alfabetica (para inverso colocar -)
        ordering = ['id_pedido']