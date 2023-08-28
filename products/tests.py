import unittest
from django.test import Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Category, Template
from .views import all_products, templates, product_detail, template_detail

class ProductViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(
            name='TestProduct',
            description='Test description',
            category=self.category,
            price=10.99
        )
        self.template = Template.objects.create(
            name='TestTemplate',
            description='Test template description',
            price=19.99
        )

    def test_all_products_view(self):
        request = self.factory.get(reverse('all_products'))
        request.user = self.user
        response = all_products(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertIn('products', response.context)

    def test_templates_view(self):
        request = self.factory.get(reverse('templates'))
        request.user = self.user
        response = templates(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/templates.html')
        self.assertIn('products', response.context)

    def test_product_detail_view(self):
        request = self.factory.get(reverse('product_detail', args=[self.product.id]))
        request.user = self.user
        response = product_detail(request, product_id=self.product.id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertIn('product', response.context)

    def test_template_detail_view(self):
        request = self.factory.get(reverse('template_detail', args=[self.template.id]))
        request.user = self.user
        response = template_detail(request, product_id=self.template.id)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/template_detail.html')
        self.assertIn('product', response.context)

if __name__ == '__main__':
    unittest.main()
