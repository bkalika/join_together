# Generated by Django 3.1.2 on 2020-11-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201101_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernet',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='usernet',
            name='github',
            field=models.CharField(blank=True, max_length=550, null=True),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]