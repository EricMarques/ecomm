# Generated by Django 3.0.7 on 2020-06-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200616_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('dinheiro', 'Dinheiro'), ('credito', 'Cartão de Crédito'), ('debito', 'Cartão de Débito')], help_text='Formas de pagamento', max_length=50, verbose_name='Forma de Pagamento'),
        ),
    ]
