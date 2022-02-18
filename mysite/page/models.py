from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category)
    in_stock = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличие)"
        return s

    def save(self, *args, **kwargs):
        # Выполняем дополнительные действия перед сохранением записи
        # Обязательно вызываем метод save родителя,
        # который, собственно, выполняет сохранение записи.
        # Если этого не сделать, запись не будет сохранена
        super(Good, self).save(*args, **kwargs)

        # Выполняем какие-либо действия перед удалением записи


class Meta:
    ordering = ["-price", "name"]
    unique_together = ("category", "name", "price")
    verbose_name = "товар"
    verbose_name_plural = "товары"

class Parent(models.Model):
    ...


class Child(models.Model):
    parent = models.OneToOneField(Parent)
# Create your models here.
