
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_game_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating_votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
