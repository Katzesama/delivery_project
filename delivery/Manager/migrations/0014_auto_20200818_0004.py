# Generated by Django 3.0.5 on 2020-08-18 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0013_order_order_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='detail',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('detail', models.CharField(max_length=500, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Order')),
            ],
        ),
    ]
