# Generated by Django 5.1.6 on 2025-02-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_name', models.CharField(max_length=100)),
                ('rec_img', models.ImageField(upload_to='receipe')),
                ('rec_desc', models.TextField()),
            ],
        ),
    ]
