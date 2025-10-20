from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Початкова (стара) ціна для відображення знижки
    original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    screenshot = models.ImageField(upload_to='images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    # Simple 0-5 rating that can be shown as stars
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    rating_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def discount_percent(self):
        try:
            if self.original_price and self.original_price > 0 and self.price is not None and self.original_price > self.price:
                return int(round(100 - (float(self.price) / float(self.original_price) * 100)))
        except Exception:
            return None
        return None

    @property
    def rating_int(self):
        try:
            return int(round(float(self.rating or 0)))
        except Exception:
            return 0

    def apply_rating(self, value: int):
        """Register a new rating (1-5) and update the average."""
        try:
            value = int(value)
        except (TypeError, ValueError):
            return
        value = max(1, min(5, value))
        total = float(self.rating or 0) * int(self.rating_votes or 0)
        total += value
        self.rating_votes = int(self.rating_votes or 0) + 1
        self.rating = round(total / self.rating_votes, 1)
        self.save(update_fields=['rating', 'rating_votes'])

    class Meta:
        unique_together = (('title', 'platform'),)
        indexes = []
