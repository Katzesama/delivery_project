# Generated by Django 3.0.5 on 2020-08-16 21:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0011_auto_20200815_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]