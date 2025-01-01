
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

    
    

class Resource(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')    
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)  # e.g., 'Primary', 'Secondary', 'Tertiary'
    trimester = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.title   

