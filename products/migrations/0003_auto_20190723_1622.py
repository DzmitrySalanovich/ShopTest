# Generated by Django 2.2.3 on 2019-07-23 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190723_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Category'),
        ),
    ]
