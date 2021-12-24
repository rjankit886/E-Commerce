# Generated by Django 3.2.4 on 2021-08-25 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('address1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('color', models.CharField(default=None, max_length=20)),
                ('size', models.CharField(default=None, max_length=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('basePeice', models.FloatField()),
                ('discount', models.FloatField(blank=True, default=0, null=True)),
                ('finalPrice', models.FloatField(blank=True, default=0, null=True)),
                ('red', models.BooleanField(blank=True, default=False, null=True)),
                ('green', models.BooleanField(blank=True, default=False, null=True)),
                ('black', models.BooleanField(blank=True, default=False, null=True)),
                ('white', models.BooleanField(blank=True, default=False, null=True)),
                ('pink', models.BooleanField(blank=True, default=False, null=True)),
                ('xs', models.BooleanField(blank=True, default=False, null=True)),
                ('s', models.BooleanField(blank=True, default=False, null=True)),
                ('m', models.BooleanField(blank=True, default=False, null=True)),
                ('l', models.BooleanField(blank=True, default=False, null=True)),
                ('xl', models.BooleanField(blank=True, default=False, null=True)),
                ('xxl', models.BooleanField(blank=True, default=False, null=True)),
                ('img1', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('img2', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('img3', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('img4', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('img5', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default=None, max_length=20)),
                ('bankName', models.CharField(blank=True, default=None, max_length=50)),
                ('ifscCode', models.CharField(blank=True, default=None, max_length=20)),
                ('accountNumber', models.CharField(blank=True, default=None, max_length=20)),
                ('total', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('name', models.CharField(default=None, max_length=50)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(blank=True, default=None, max_length=254)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('mode', models.CharField(default=None, max_length=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product'),
        ),
    ]
