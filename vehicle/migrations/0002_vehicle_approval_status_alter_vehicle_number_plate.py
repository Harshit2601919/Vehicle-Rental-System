# Generated by Django 5.0.2 on 2024-03-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='approval_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_plate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
