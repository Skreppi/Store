import os

import django
from django.test import TestCase
from django.urls import reverse

from products.models import Products

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()


class HomeViewTestCase(TestCase):

    def test_template(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertEqual(response.template_name[0], 'products/home.html')
        self.assertTemplateUsed(response, 'products/home.html')


class ProductsListViewTestCase(TestCase):

    def test_list(self):
        path = reverse('products')
        response = self.client.get(path)

        products = Products.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context_data['object_list']), list(products))
