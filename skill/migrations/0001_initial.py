# Generated by Django 4.0.5 on 2022-09-28 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('keydata', models.CharField(db_index=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('keydata', models.CharField(db_index=True, max_length=200, null=True)),
                ('skill', models.CharField(blank=True, max_length=200, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.member', verbose_name='member name')),
            ],
        ),
    ]
