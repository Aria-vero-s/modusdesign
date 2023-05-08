# Generated by Django 3.2 on 2023-05-02 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230501_1907'),
        ('bag', '0005_auto_20230502_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagitem',
            name='bag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bag.bag'),
        ),
        migrations.AlterField(
            model_name='bagitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='bagitem',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.service'),
        ),
    ]
