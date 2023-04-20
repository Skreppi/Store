from django import template

from products.models import ProductsCategory

register = template.Library()


@register.inclusion_tag('products/categories_tpl.html')
def menu_tag():
    categories = ProductsCategory.objects.all()
    return ({'categories': categories})
