# Generated by Django 2.2.12 on 2021-08-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_match_players'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arena',
            options={'verbose_name': 'Pelikenttä', 'verbose_name_plural': 'Pelikentät'},
        ),
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name': 'Pelaaja', 'verbose_name_plural': 'Pelaajat'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Peli', 'verbose_name_plural': 'Pelit'},
        ),
        migrations.AlterModelOptions(
            name='parent',
            options={'verbose_name': 'Vanhempi', 'verbose_name_plural': 'Vanhemmat'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Toimitsijatehtävä', 'verbose_name_plural': 'Toimitsijatehtävät'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('KELLO', 'Kello'), ('KUULUTUS', 'Kuulutus'), ('JÄÄHY', 'Jäähy'), ('PÖYTÄKIRJA', 'Pöytäkirjä'), ('TITU', 'Titu'), ('KUVAAJA', 'Kuvaaja')], default='JÄÄHY', max_length=64),
        ),
        migrations.AlterField(
            model_name='child',
            name='parents',
            field=models.ManyToManyField(blank=True, to='app.Parent'),
        ),
    ]