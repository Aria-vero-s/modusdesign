from django.db import models
from products.models import Product
from products.models import Service
from django.contrib.auth.models import User


class Bag(models.Model):
    session_key = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.total_items} item{'s' if self.total_items != 1 else ''} in bag"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @classmethod
    def get_bag(cls, request):
        bag = None
        if request.user.is_authenticated:
            # If the user is authenticated, use their user account as the bag owner
            bag, created = cls.objects.get_or_create(user=request.user)
        else:
            # If the user is anonymous, use the session key to identify the bag
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key
            bag, created = cls.objects.get_or_create(session_key=session_key)
        return bag


class BagItem(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name='items', null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name and self.service.name} in bag for {self.user.username}"
