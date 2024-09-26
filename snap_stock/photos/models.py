from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='photos/')
    uploaded_at = models.DateTimeField("Дата загрузки", auto_now_add=True)
    # uploader = models.ForeignKey(User, verbose_name="Загрузил", on_delete=models.CASCADE)
    alerts = models.CharField("Оповещения", max_length=255)
    acceptable_level = models.IntegerField("Допустимый уровень", default=0)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
