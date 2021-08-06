# Generated by Django 2.2.12 on 2021-08-06 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210806_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='jäähy_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_jäähy_1', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='jäähy_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_jäähy_2', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='kello',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kello', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='kuulutus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kuulutus', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='kuvaaja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kuvaaja', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='pöytäkirja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_pöytäkirja', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='match',
            name='titu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_titu', to='app.Parent'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('Kello', 'Kello'), ('Kuulutus', 'Kuulutus'), ('Jäähy', 'Jäähy'), ('Pöytäkirja', 'Pöytäkirja'), ('Titu', 'Titu'), ('Kuvaaja', 'Kuvaaja')], default='Jäähy', max_length=64, unique=True),
        ),
    ]
