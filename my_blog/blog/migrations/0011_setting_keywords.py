# Generated by Django 5.1.6 on 2025-03-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='keywords'),
        ),
    ]
