# Generated by Django 4.2.1 on 2023-06-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0002_alter_song_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='singer',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
