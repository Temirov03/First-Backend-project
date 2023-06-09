# Generated by Django 4.2 on 2023-04-21 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(default='')),
                ('value', models.CharField(choices=[('yaxshi', 'Ijobiy'), ('yomon', 'Salbiy')], max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=155)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Mahsulot', 'verbose_name_plural': 'Mahsulotlar'},
        ),
    ]
