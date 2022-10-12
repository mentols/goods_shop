# Generated by Django 4.1.1 on 2022-10-10 16:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=255)),
                ('availability', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.CharField(max_length=2000)),
                ('description_tittle', models.CharField(max_length=255)),
                ('size', models.PositiveSmallIntegerField(choices=[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'Xl')], default=1)),
                ('cover', models.ImageField(null=True, upload_to='img/%Y-%m-%d/')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('sale', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100), django.core.validators.MinValueValidator(limit_value=0)])),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.category')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.address')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='img/%Y-%m-%d/')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.good')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deliver', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.customer')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.address')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.good')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.order')),
            ],
        ),
    ]