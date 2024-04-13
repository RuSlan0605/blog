from django.db import models
from django.urls import reverse

class Category(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', args=[self.id])
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

class Blog(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id, self.slug])

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
