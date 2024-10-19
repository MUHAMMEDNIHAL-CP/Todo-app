# Generated by Django 5.0.7 on 2024-07-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('create_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
