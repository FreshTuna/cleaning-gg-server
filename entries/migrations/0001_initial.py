# Generated by Django 3.1.7 on 2022-01-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0004_auto_20220106_2158'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Entry',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('match_id', models.IntegerField()),
        #         ('leader_yn', models.BooleanField(default=False)),
        #         ('team', models.CharField(choices=[('RED', 'Red'), ('BLUE', 'Blue')], max_length=20, null=True)),
        #         ('created_at', models.DateTimeField(auto_now_add=True)),
        #         ('updated_at', models.DateTimeField(auto_now=True)),
        #         ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
        #     ],
        #     options={
        #         'db_table': 'entries',
        #     },
        # ),
    ]
