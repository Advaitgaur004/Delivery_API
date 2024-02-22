# Generated by Django 5.0.2 on 2024-02-21 23:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, help_text='Add your Email', max_length=35, null=True, unique=True, validators=[django.core.validators.EmailValidator(message='Invalid email address.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25),
        ),
    ]
