# Generated by Django 3.1.5 on 2021-01-21 23:43

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('contact', models.CharField(max_length=15, verbose_name='contact')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=20, verbose_name='user role')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
