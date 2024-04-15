# Generated by Django 4.2.7 on 2024-04-14 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0005_vehicle_name_alter_vehicle_images_delete_renthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='canceledOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('automobileId', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlePrev', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(blank=True, max_length=375, null=True)),
                ('question', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUpPlace', models.CharField(max_length=105, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel',
            field=models.CharField(choices=[('P', 'Petrol'), ('D', 'Diesel')], default='D', max_length=1),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=70, null=True)),
                ('customerID', models.CharField(max_length=50, null=True)),
                ('carModel', models.CharField(max_length=70, null=True)),
                ('automobileId', models.CharField(max_length=10, null=True)),
                ('price', models.IntegerField(null=True)),
                ('startRent', models.DateField(null=True)),
                ('endRent', models.DateField(null=True)),
                ('orderDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('fullFuel', models.BooleanField(blank=True, default=False, null=True)),
                ('insurance', models.BooleanField(blank=True, default=False, null=True)),
                ('payed', models.BooleanField(default=False, null=True)),
                ('pickUp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.location')),
            ],
        ),
    ]