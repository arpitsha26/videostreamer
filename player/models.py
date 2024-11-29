import os
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

def validate_mp4_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    if ext.lower() != '.mp4':
        raise ValidationError("Only .mp4 files are allowed.")
    
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    
class Movie(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed'),
    )
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=500, blank=True)
    description = models.TextField()
    release_date=models.DateField()
    categories=models.ManyToManyField(Category,related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies_generes")
    video = models.FileField(upload_to="videos",validators=[validate_mp4_extension])
    poster=models.ImageField(upload_to='movie_posters/',  blank=True,null=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    hls = models.CharField(max_length=500,blank=True,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    is_running = models.BooleanField(default=False)
  
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
