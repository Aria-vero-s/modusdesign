import unittest
from django.urls import reverse
from django.test import TestCase, Client
from .forms import ContactForm  # Import your ContactForm class
from .models import Contact  # Import your Contact model
from django.contrib.messages import get_messages

class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view_GET(self):
        response = self.client.get(reverse('home'))

    def test_index_view_POST_invalid_form(self):
        data = {'invalid_field': 'invalid_value'}
        response = self.client.post(reverse('home'), data)

    def test_index_view_POST_valid_form(self):
        data = {'valid_field': 'valid_value'}
        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIsInstance(response.context['form'], ContactForm)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Message sent! You will soon receive a reply by email.')

if __name__ == '__main__':
    unittest.main()
