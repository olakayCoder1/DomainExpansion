# Generated by Django 4.0.4 on 2022-09-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='profiles/avatar.svg', null=True, upload_to='profiles/'),
        ),
    ]
