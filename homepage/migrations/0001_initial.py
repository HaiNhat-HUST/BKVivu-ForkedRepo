# Generated by Django 4.2.7 on 2023-12-28 17:31

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('raw_password', models.CharField(max_length=50, null=True)),
                ('role', models.CharField(choices=[('sharer', 'Người chia sẻ'), ('manager', 'Người quản lý')], max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 12, 29, 0, 31, 3, 629180))),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to=homepage.models.img_path_bill)),
                ('status', models.CharField(default='Waiting', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(default=homepage.models.generate_unique_post_id, max_length=100, unique=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('name_stripped', models.CharField(max_length=50, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 12, 29, 0, 31, 3, 629180))),
                ('location', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.account')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('name_stripped', models.TextField(max_length=50, null=True)),
                ('type', models.CharField(choices=[('food', 'Đồ ăn'), ('bun dau', 'Bún đậu'), ('com rang', 'Cơm rang'), ('nem nuong', 'Nem nướng'), ('cong vien', 'Công viên'), ('bao tang', 'Bảo tàng'), ('service', 'Dịch vụ khác')], max_length=10)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(default='default.jpg', upload_to=homepage.models.img_path_product)),
                ('describe', models.TextField(null=True)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 12, 29, 0, 31, 3, 613382))),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.account')),
                ('name', models.TextField(max_length=50)),
                ('name_stripped', models.TextField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('avatar', models.ImageField(default='noavatar.png', upload_to=homepage.models.img_path_avt)),
                ('bank', models.ImageField(default='noavatar.png', upload_to=homepage.models.img_path_bank)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('t_open', models.TimeField(default='0:00')),
                ('t_closed', models.TimeField(default='23:59')),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('ward', models.CharField(max_length=50, null=True)),
                ('bio', models.TextField(max_length=1500, null=True)),
                ('num_votes', models.IntegerField(default=0, null=True)),
                ('avgStar', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Sharer',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.account')),
                ('name', models.CharField(max_length=50, verbose_name='fullname')),
                ('age', models.IntegerField(null=True)),
                ('avatar', models.ImageField(default='noavatar.png', upload_to=homepage.models.img_path_avt)),
                ('city', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('ward', models.CharField(max_length=50, null=True)),
                ('bio', models.TextField(max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.bill')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.product')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=homepage.models.imgs_path)),
                ('isDelete', models.BooleanField(default=False)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.account')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.post')),
            ],
        ),
        migrations.CreateModel(
            name='StarVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.account')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.manager')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.manager'),
        ),
        migrations.AddField(
            model_name='post',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.manager'),
        ),
        migrations.AddField(
            model_name='bill',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.manager'),
        ),
        migrations.AddField(
            model_name='bill',
            name='sharer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.sharer', verbose_name='Người mua'),
        ),
    ]
