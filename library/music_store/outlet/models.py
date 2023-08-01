from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    singer = models.CharField(null=True, max_length=100)
    slug = models.SlugField(default='', null=False)

    
def save(self, *args,  **kwargs) :
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

       
    
def __str__(self):
    return f'{self.title} ({self.rating})'