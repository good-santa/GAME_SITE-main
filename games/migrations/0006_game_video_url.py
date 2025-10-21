
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_merge_images_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
