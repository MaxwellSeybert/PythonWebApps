# Generated by Django 4.1.2 on 2022-11-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0005_alter_superhero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
