# Generated by Django 2.2.5 on 2019-09-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstName', models.CharField(max_length=50, verbose_name="User's first name")),
                ('lastName', models.CharField(max_length=50, verbose_name="User's last name")),
                ('username', models.CharField(max_length=50, unique=True, verbose_name="User's username")),
                ('pictureUlr', models.CharField(default='https://randomuser.me/api/portraits/women/60.jpg', max_length=254, verbose_name="User's picture")),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name="User's email")),
                ('password', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
