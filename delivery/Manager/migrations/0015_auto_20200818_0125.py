# Generated by Django 3.0.5 on 2020-08-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0014_auto_20200818_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]