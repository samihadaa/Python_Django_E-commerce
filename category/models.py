from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

#changing admin category name.
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_By_Categorie', args=[self.slug])
    def __str__(self):
        return self.category_name