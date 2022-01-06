# Generated by Django 3.1.7 on 2022-01-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='line',
            field=models.CharField(choices=[('TOP', 'Top'), ('JUNGLE', 'Jungle'), ('MID', 'Mid'), ('ADC', 'Adc'), ('SUPPORT', 'Support')], max_length=20, null=True),
        ),
    ]