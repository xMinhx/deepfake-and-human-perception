# Generated by Django 3.1.3 on 2021-01-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_pause', models.IntegerField()),
                ('replay', models.IntegerField()),
                ('fullscreen', models.IntegerField()),
                ('playback', models.IntegerField()),
                ('duration_in_sec', models.IntegerField()),
                ('text', models.TextField(max_length=300)),
            ],
            options={
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.TextField(primary_key=True, serialize=False)),
                ('gdrive_id', models.TextField(unique=True)),
                ('onedrive_id', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]
