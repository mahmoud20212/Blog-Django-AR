# Generated by Django 5.1.6 on 2025-03-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_about_options_alter_setting_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_icon',
            field=models.ImageField(help_text='The Site Icon is what you see in browser tabs, bookmark bars, and within the WordPress mobile apps. It should be square and at least 512 by 512 pixels.', upload_to='logo_pics', verbose_name='site icon'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_title',
            field=models.CharField(max_length=255, verbose_name='site title'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='tagline',
            field=models.CharField(help_text='In a few words, explain what this site is about. Example: “Just another WordPress site.”', max_length=255, verbose_name='tagline'),
        ),
    ]
