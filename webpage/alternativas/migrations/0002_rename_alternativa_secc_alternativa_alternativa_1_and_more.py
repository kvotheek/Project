# Generated by Django 4.0.6 on 2022-07-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alternativas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secc_alternativa',
            old_name='alternativa',
            new_name='alternativa_1',
        ),
        migrations.AddField(
            model_name='secc_alternativa',
            name='alternativa_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='secc_alternativa',
            name='alternativa_3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='secc_alternativa',
            name='alternativa_4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='secc_alternativa',
            name='alternativa_5',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
