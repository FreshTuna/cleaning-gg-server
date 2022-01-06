# Generated by Django 3.1.7 on 2022-01-05 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('start_at', models.DateTimeField()),
                ('win_team', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue')], max_length=20)),
                ('status', models.CharField(choices=[('MATCHING', 'Matching'), ('PLAYING', 'Playing'), ('COMPLETE', 'Complete'), ('CANCLED', 'Cancled')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'matches',
            },
        ),
    ]