# Generated by Django 5.0.9 on 2024-10-15 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0010_subscriptionprice_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptionprice',
            options={'ordering': ['orders', 'featured', '-updated']},
        ),
    ]