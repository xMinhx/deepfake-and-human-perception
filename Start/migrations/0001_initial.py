# Generated by Django 3.1.3 on 2021-01-08 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('label_id', models.IntegerField(primary_key=True, serialize=False)),
                ('label_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'class_label',
            },
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('label_id', models.IntegerField(primary_key=True, serialize=False)),
                ('label_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'difficulty',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('label_name', models.TextField(unique=True)),
                ('label_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Scoreboard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('scores', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Testgroup',
            fields=[
                ('label_id', models.IntegerField(primary_key=True, serialize=False)),
                ('label_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'testgroup',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('pixel_width', models.IntegerField()),
                ('pixel_height', models.IntegerField()),
                ('fps', models.IntegerField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Start.gender')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('testgroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Start.testgroup')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
