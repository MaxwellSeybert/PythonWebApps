# Generated by Django 4.1.2 on 2022-11-17 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_photo_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.photo'),
        ),
    ]
