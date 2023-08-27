import unittest
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.messages.storage.fallback import FallbackStorage
from products.models import Product
from bag.views import add_to_bag

class TestAddToBagFunction(unittest.TestCase):
    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(name='Test Product', price=10.0)

        # Create a request factory
        self.factory = RequestFactory()

    def _setup_request(self, url, method='get', data=None, session=None):
        request = getattr(self.factory, method)(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        if session:
            request.session.update(session)
        request.session.save()
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        request._messages = messages
        messages.middleware = MessageMiddleware()
        return request


    def test_add_to_bag_with_size(self):
        # Create a POST request with data
        data = {
            'product_size': 'M',
            'quantity': 2,
            'redirect_url': reverse('view_bag')
        }
        request = self._setup_request(reverse('add_to_bag', args=[self.product.pk]), 'post', data)

        # Call the view function
        response = add_to_bag(request, self.product.pk)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
