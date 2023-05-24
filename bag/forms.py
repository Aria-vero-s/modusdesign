from django import forms
from products.models import Product

class ServiceForm(forms.Form):
    service_choices = [
        ('logo', 'logo'),
        ('promotional', 'promotional'),
        ('stationary', 'stationary'),
        ('packaging', 'packaging'),
        ('blog', 'blog'),
        ('portfolio', 'portfolio'),
        ('small-business', 'small-business'),
        ('e-commerce', 'e-commerce'),
        ('illustration', 'illustration'),
        ('non-fiction', 'non-fiction'),
        ('magazine', 'magazine'),
        ('storybook', 'storybook'),
        ('logo2', 'logo2'),
        ('promotional2', 'promotional2'),
        ('website2', 'website2'),
        ('illustration2', 'illustration2'),
        # add more services here
    ]
    services = forms.MultipleChoiceField(choices=service_choices, widget=forms.CheckboxSelectMultiple)


class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.RadioSelect)
