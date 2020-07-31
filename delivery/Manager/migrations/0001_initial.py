# Generated by Django 3.0.5 on 2020-07-31 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(default='static/Manager/images/defaultimage.jpg', upload_to='dish_images/')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ordered_time', models.DateTimeField(auto_now_add=True)),
                ('detail', models.CharField(max_length=2000, null=True)),
                ('deliver_address', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_phone', models.CharField(blank=True, max_length=12, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=50, null=True)),
                ('order_num', models.IntegerField()),
                ('status', models.CharField(choices=[('处理中', '处理中'), ('送餐中', '送餐中'), ('完成', '完成'), ('退款中', '退款中'), ('已退款', '已退款')], default='处理中', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='No Name', max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('wechat', models.CharField(max_length=20)),
                ('wechatcode', models.ImageField(blank=True, null=True, upload_to='wechat_code/')),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Manager.Restaurant')),
                ('user', models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='选项', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='OpenningTime',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('weekday', models.IntegerField(choices=[(1, '星期一'), (2, '星期二'), (3, '星期三'), (4, '星期四'), (5, '星期五'), (6, '星期六'), (7, '星期天')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.Kind'),
        ),
    ]
