# Generated by Django 3.0.5 on 2020-04-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
