# Generated by Django 2.0.3 on 2018-04-17 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('hostname', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('address', models.GenericIPAddressField()),
                ('displays', models.IntegerField(default=2)),
                ('ram', models.IntegerField(default=0)),
                ('cpu', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('desk_number', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('data_points', models.IntegerField(default=6)),
                ('power_points', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='DRUser',
            fields=[
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('business_unit', models.CharField(max_length=5)),
                ('desk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Desk')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Computer')),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Room'),
        ),
        migrations.AddField(
            model_name='computer',
            name='desk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Desk'),
        ),
    ]
