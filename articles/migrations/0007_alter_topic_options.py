# Generated by Django 4.2.14 on 2024-11-07 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_options_alter_topic_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name'], 'verbose_name': 'Topic'},
        ),
    ]
