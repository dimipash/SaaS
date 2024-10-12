# Generated by Django 5.0.9 on 2024-10-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm')],
            },
        ),
    ]
