# Generated by Django 5.0.6 on 2024-06-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0059_author_profile_rename_writer_info_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True, verbose_name=''),
        ),
    ]