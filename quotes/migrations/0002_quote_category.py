# Generated by Django 5.0.6 on 2024-06-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
    ]