# Generated by Django 4.2.6 on 2023-12-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_managers_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article', models.CharField(max_length=1000)),
                ('Title', models.CharField(max_length=200)),
            ],
        ),
    ]
