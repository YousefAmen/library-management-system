# Generated by Django 5.0.3 on 2024-06-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default=None, max_length=100, unique=True, verbose_name='Book Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=None, max_length=100, unique=True, verbose_name=''),
        ),
    ]
