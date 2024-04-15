# Generated by Django 4.2.7 on 2024-04-14 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('email', models.CharField(max_length=25, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('profilePic', models.ImageField(blank=True, default='basicUser.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
