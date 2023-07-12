from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    singer = models.CharField(null=True, max_length=100)
    
    
    
def __str__(self):
    return f'{self.title} ({self.rating})'