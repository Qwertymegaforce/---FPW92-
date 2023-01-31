# Generated by Django 4.1.3 on 2022-12-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('text', models.TextField(default='Здесь ничего не написано')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]