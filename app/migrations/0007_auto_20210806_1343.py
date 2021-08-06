# Generated by Django 2.2.12 on 2021-08-06 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210806_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='jäähy_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_jäähy_1', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='jäähy_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_jäähy_2', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='kello',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kello', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='kuulutus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kuulutus', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='kuvaaja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_kuvaaja', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='pöytäkirja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_pöytäkirja', to='app.Parent'),
        ),
        migrations.AddField(
            model_name='match',
            name='titu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_titu', to='app.Parent'),
        ),
    ]
