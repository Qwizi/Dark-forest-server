# Generated by Django 4.2 on 2023-05-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_server', '0003_rename_user_stats_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
