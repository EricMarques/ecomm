from django.db import models
from django.db.models import (
    Q,
    QuerySet
    )


class ProductManager(models.Manager):
    def with_text(self, text: str) -> QuerySet:
        '''
            Pesquisa nos produtos cujo filtro seja **"text"**.
            
            :param text: Texto que será usado na pesquisa.

            :return: QuerySet com o filtro aplicado.
        '''
        queryset = self.get_queryset().filter(name__contains=text)
        return queryset
    
    def expensive_products(self) -> QuerySet:
        '''
            Filtro de produtos cujo preço seja maior que 500,00
        '''
        return self.get_queryset().filter(price__gte=500)

    def cheap_products(self) -> QuerySet:
        '''
            Retorna a lista dos produtos mais baratos.
        '''
        return self.get_queryset().filter(
            category__name__contains='categoria',
            price__lte=15
        )

    def cat1_or_expensive_products(self) -> QuerySet:
        '''
            Retorna a lista dos produtos mais caros de uma determinada categoria.
        '''
        query_filter = Q(category__name='Categoria 1') | Q(price__gte=500)
        queryset = self.get_queryset().filter(query_filter)

        print(queryset.query)
        return queryset
    
    def test_fiunction(self):
        self.with_text('')
        self.expensive_products('')
        self.cheap_products('') 
        self.cat1_or_expensive_products('')


class Category(models.Model):
    name = models.CharField(verbose_name='Categoria',
                            max_length=50,
                            blank=False,
                            null=False)

    description = models.TextField(verbose_name='Descrição',
                                   max_length=200,
                                   blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = 'Categorias'


# Create your models here.
class Product(models.Model):
    '''
        Model contendo todos os campos necessários
        para o cadastro de produtos no ecomm.
    '''
    objects = ProductManager()
    name = models.CharField(verbose_name='Nome',
                            max_length=100,
                            blank=False,
                            null=False)

    description = models.TextField(verbose_name='Descrição',
                                   max_length=200,
                                   blank=True,
                                   null=True)

    price = models.DecimalField(verbose_name='Preço',
                                max_digits=8,
                                decimal_places=2,
                                blank=False,
                                null=False)

    category = models.ForeignKey(Category,
                                 verbose_name='Categoria',
                                 on_delete=models.DO_NOTHING,
                                 related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito')
    ]
    name = models.CharField(verbose_name='Nome',
                            max_length=100,
                            blank=False,
                            null=False)
    payment = models.CharField(verbose_name='Forma de Pagamento',
                               max_length=50,
                               choices=PAYMENT_CHOICES,
                               blank=False,
                               null=False,
                               help_text='Formas de pagamento')
    products = models.ManyToManyField(Product)
    
    @property
    def total_amount(self):
        return sum([product.price for product in self.products.all()])

    def __str__(self):
        return f'{self.name} - {self.total_amount}'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
