# Generated by Django 4.1.7 on 2023-06-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_address_alter_users_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('s', 'seller'), ('c', 'customer')], default=('c', 'customer'), max_length=1),
        ),
    ]
