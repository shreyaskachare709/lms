# Generated by Django 4.0.4 on 2022-10-31 14:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('typeofbook', models.CharField(max_length=100)),
                ('is_deleted', models.CharField(default='n', max_length=5)),
            ],
            managers=[
                ('CustomManager', django.db.models.manager.Manager()),
            ],
        ),
    ]