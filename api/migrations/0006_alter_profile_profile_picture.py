# Generated by Django 4.2.6 on 2023-12-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media\\images\\default.jpg', upload_to='images'),
        ),
    ]
