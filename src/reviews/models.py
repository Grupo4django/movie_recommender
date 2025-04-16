from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    """Detailed movie reviews"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Write your review here")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rating from 1 to 10"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False, help_text="Approved by moderator")
    media = models.ImageField(upload_to='reviews/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('movie', 'user', 'title')

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"
