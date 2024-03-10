# Generated by Django 5.0.2 on 2024-02-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default='10')),
                ('species', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=30)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'Pet',
            },
        ),
    ]