# Generated by Django 4.0.1 on 2022-05-27 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.boss')),
            ],
        ),
    ]