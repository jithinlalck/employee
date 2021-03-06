# Generated by Django 4.0.3 on 2022-03-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='gallery')),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
