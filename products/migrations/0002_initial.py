# Generated by Django 5.0.6 on 2024-05-22 06:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproducts'),
        ),
        migrations.AddField(
            model_name='cart',
            name='clothes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clothes'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='watch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.clothes'),
        ),
    ]
