# Generated by Django 4.0.4 on 2022-05-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0003_alter_application_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]