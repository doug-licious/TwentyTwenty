# Generated by Django 2.0.3 on 2018-03-29 02:01

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=10)),
                ('address', models.GenericIPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_number', models.IntegerField()),
                ('data_points', models.IntegerField()),
                ('power_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DR_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(choices=[('IPC', 'IPC'), ('CISCO', 'CISCO')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('computer', models.ManyToManyField(to='desks.Computer')),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='desks.DR_User'),
        ),
        migrations.AddField(
            model_name='computer',
            name='desk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='desks.Desk'),
        ),
        migrations.AddField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='desks.DR_User'),
        ),
    ]