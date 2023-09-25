from django.contrib import admin
from .models import CityName, Project, ProjectImage,Blogs, BlogCategories

# ProjectImage modelini Project modeli ile birleştiren inline sınıfı
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3  # Ekstra boş alan sayısı

# Project modelini admin panelinde nasıl gösterileceğini belirleyen sınıf
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'city_name')  # Listede hangi alanların gösterileceğini belirliyoruz
    search_fields = ['title', 'city_name__city']  # Hangi alanlara göre arama yapabileceğimizi belirliyoruz


# Özel bir ModelAdmin sınıfı ile
class CityNameAdmin(admin.ModelAdmin):
    list_display = ['city']
    search_fields = ['city']


# Ya da sadece modeli ekleyerek
# admin.site.register(CityName)

# Model'leri admin paneline ekliyoruz
admin.site.register(CityName, CityNameAdmin)
admin.site.register(Project, ProjectAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Listelenen alanlar
    search_fields = ('title', 'author')  # Arama yapılacak alanlar
    list_filter = ('published_date',)  # Filtreleme yapılacak alanlar
    date_hierarchy = 'published_date'  # Tarih hiyerarşisi

class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(BlogCategories, BlogCategoriesAdmin)

