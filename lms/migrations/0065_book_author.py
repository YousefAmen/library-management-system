# Generated by Django 5.0.6 on 2024-07-02 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0064_remove_category_achievements_remove_category_awardes_and_more'),
        ('members', '0002_author_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.author_profile'),
        ),
    ]
