# Generated by Django 4.0.2 on 2022-05-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_personvisit_delete_userdata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personvisit',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
