# Generated by Django 5.0.3 on 2024-05-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0008_alter_vehicle_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_status',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='images',
            field=models.ImageField(blank=True, default='images/default.webp', null=True, upload_to='images/'),
        ),
    ]