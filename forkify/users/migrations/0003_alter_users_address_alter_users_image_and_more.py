# Generated by Django 4.1.7 on 2023-06-13 07:32

from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='users.address'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=enumchoicefield.fields.EnumChoiceField(default=users.models.Role(2), enum_class=users.models.Role, max_length=8),
        ),
    ]
