from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        product = Product.objects.create(
            name='Teste Produto',
            description='Teste Descrição',
            price=0.23,
            category_id=1
        )

        self.assertEqual(str(product), 'Teste Produto')