from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=254, null=True, blank=True)
    lname = models.CharField(max_length=254)
    email = models.EmailField(max_length = 254)
    comment = models.TextField(max_length = 600)

    def __str__(self):
        return self.email
