# Generated by Django 4.0.5 on 2023-06-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='current_player',
        ),
        migrations.AddField(
            model_name='game',
            name='current_players',
            field=models.IntegerField(default=1),
        ),
    ]
