# Generated by Django 2.2.12 on 2021-08-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210806_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('Kello', 'Kello'), ('Kuulutus', 'Kuulutus'), ('Jäähy', 'Jäähy'), ('Pöytäkirjä', 'Pöytäkirjä'), ('Titu', 'Titu'), ('Kuvaaja', 'Kuvaaja')], default='Jäähy', max_length=64, unique=True),
        ),
    ]
