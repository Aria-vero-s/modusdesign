# import unittest
# from django.test import TestCase, RequestFactory, Client
# from django.urls import reverse
# from django.contrib.sessions.middleware import SessionMiddleware
# from django.contrib.messages.middleware import MessageMiddleware
# from django.contrib.messages.storage.fallback import FallbackStorage
# from checkout.views import checkout
# from bag.views import add_to_bag
# from bag.contexts import bag_contents


# class TestCheckoutFunction(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#         self.checkout_url = reverse('checkout')

#     def test_checkout_view_get(self):
#         # Create a bag session
#         self.client.post(reverse('add_to_bag', args=[product_id]), data={'quantity': 1})

#         # Create a GET request
#         request = self.factory.get(self.checkout_url)
        
#         # Add session middleware to the request
#         middleware = SessionMiddleware()
#         middleware.process_request(request)
        
#         # Add messages middleware to the request
#         messages = FallbackStorage(request)
#         setattr(request, '_messages', messages)

#         # Attach the bag session to the request
#         request.session['bag'] = {'product_id': 1}  # Replace with your actual bag content

#         response = self.client.get(self.checkout_url, follow=True)  # Follow the redirect

#         # Check if the response status code is 200 after following the redirect
#         self.assertEqual(response.status_code, 200)

#         # Check if the correct template is used
#         self.assertTemplateUsed(response, 'checkout/checkout.html')

# if __name__ == '__main__':
#     unittest.main()
