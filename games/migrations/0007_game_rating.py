
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_game_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
