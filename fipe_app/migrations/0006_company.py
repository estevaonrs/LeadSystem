# Generated by Django 5.0.1 on 2024-01-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fipe_app', '0005_alter_lead_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]
