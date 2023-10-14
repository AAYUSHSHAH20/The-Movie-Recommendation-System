# Generated by Django 4.2.4 on 2023-09-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('year', models.DecimalField(decimal_places=1, max_digits=5)),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('vote_avg', models.FloatField()),
                ('img_url', models.CharField(max_length=250)),
                ('actor', models.CharField(max_length=250)),
            ],
        ),
    ]