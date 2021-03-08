from django.db import models

class Category(models.Model):
    sort_id = models.IntegerField('Порядок', default=0)
    name = models.CharField("Название",max_length=255)
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Posts(models.Model):
    name = models.CharField("Название",max_length=255)
    url = models.SlugField(max_length=255, unique=True)
    img = models.ImageField('Фотография', upload_to='posts/', blank=True)
    description = models.TextField('Описание')
    full_text = models.TextField('Полный текст',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


