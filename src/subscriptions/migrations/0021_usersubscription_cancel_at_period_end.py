# Generated by Django 5.0.9 on 2024-10-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0020_usersubscription_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
    ]
