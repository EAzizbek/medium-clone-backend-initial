# Generated by Django 4.2.14 on 2024-11-07 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article'},
        ),
    ]