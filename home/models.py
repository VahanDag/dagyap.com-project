from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# POJECTS
class CityName(models.Model):
    city = models.CharField(verbose_name="Şehir İsmi", max_length=20)

    def __str__(self):
        return self.city

class Project(models.Model):  # Tekil isim kullanıldı
    city_name = models.ForeignKey(CityName, verbose_name="Şehir İsmi", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Kısa Başlık", max_length=100)

    def __str__(self):
        return f"{self.city_name.city} - {self.title}"  # Şehir ismini ve başlığı birlikte döndürdük

class ProjectImage(models.Model):  # Tekil isim kullanıldı
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/projects/')



# BLOGS

class BlogCategories(models.Model):
    category = models.CharField(verbose_name="Kategori", max_length=50)

    def __str__(self):
        return self.category

class Blogs(models.Model):
    title = models.CharField(verbose_name="Başlık", max_length=255)
    author = models.CharField(verbose_name="Yazar", max_length=30)
    title_image = models.ImageField(upload_to='static/img/blog/',verbose_name="Resim")
    published_date = models.DateField(verbose_name="Tarih")
    # first_place = models.TextField(verbose_name="Giriş yazısı")
    first_place = HTMLField(verbose_name="Giriş yazısı")
    quote = models.CharField(verbose_name="Vurgulanan Söz", max_length=255)
    second_place = HTMLField(verbose_name="İkinci Bölüm")
    sub_image = models.ImageField(upload_to='static/img/blog/',verbose_name="İkinci Resim")
    finished_place = HTMLField(verbose_name="Kapanış yazısı")
    category = models.ForeignKey(BlogCategories, verbose_name="Kategoriler",on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blogs, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
