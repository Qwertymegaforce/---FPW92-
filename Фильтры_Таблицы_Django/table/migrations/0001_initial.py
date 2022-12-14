# Generated by Django 4.1.3 on 2022-12-13 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('text', models.TextField(default='Здесь ничего не написано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.author')),
            ],
        ),
    ]
