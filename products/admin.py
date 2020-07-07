from django.contrib import admin
from products.models import (
    Product,
    Category,
    Order
)

from django.utils.html import format_html
from django.urls import reverse
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    def products(self, obj):
        # admin:APP_NAME_MODEL_NAME_changelist + filtro
        
        href = reverse('admin:products_product_changelist') + f'?category={obj.pk}'
        return format_html(f'<a href="{ href }">{ obj.products.count() }</a>')

    list_display = ('name', 'description', 'products')
    
    products.short_description = 'Produtos da Categoria'

class ProductModelAdmin(admin.ModelAdmin):
    '''
    # Outra forma de fazer o filtro por categoria.
    def queryset(self, request, queryset):
        category = request.GET.get('category')
        if category:
            return queryset.filter(category__pk=category)
        else:
            return queryset
    '''

    def formatted_price(self, obj):
        return f'R${obj.price}'

    formatted_price.short_description = 'Preço'

    def link_category(self, obj):
        href = reverse('admin:products_category_change', args=(obj.category.pk,))
        return format_html(f'<a href="{ href }">{ obj.category.name }</a>')

    link_category.short_description = 'Categoria'
    list_display = ('name', 'description', 'formatted_price', 'link_category')


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Order)
