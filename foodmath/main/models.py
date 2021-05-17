from django.db import models

# Create your models here.
class Product(models.Model):
    
    title = models.CharField(max_length=255, verbose_name="Наименование")
    kcal = models.FloatField(default=0, verbose_name="Калории")
    protein = models.FloatField(default=0, verbose_name="Белки")
    carb = models.FloatField(default=0, verbose_name="Углеводы")
    fat = models.FloatField(default=0, verbose_name="Жиры")
    fibre = models.FloatField(default=0, verbose_name="Клетчатка")
    vitaminC = models.FloatField(default=0, verbose_name="Витамин C")
    vitaminD = models.FloatField(default=0, verbose_name="Витамин D")
    vitaminA = models.FloatField(default=0, verbose_name="Витамин А")
    vitaminE = models.FloatField(default=0, verbose_name="Витамин Е")
    vitaminB2 = models.FloatField(default=0, verbose_name="Витамин B2")
    vitaminB5 = models.FloatField(default=0, verbose_name="Витамин B5")
    vitaminB6 = models.FloatField(default=0, verbose_name="Витамин B6")
    vitaminB9 = models.FloatField(default=0, verbose_name="Витамин B9")
    vitaminB12 = models.FloatField(default=0, verbose_name="Витамин B12")
    Fe = models.FloatField(default=0, verbose_name="Железо")
    Ca = models.FloatField(default=0, verbose_name="Кальций")
    K = models.FloatField(default=0, verbose_name="Калий")
    Mg = models.FloatField(default=0, verbose_name="Магний")
    Zn = models.FloatField(default=0, verbose_name="Цинк")
    cost = models.FloatField(default=0, verbose_name="Цена")

    def __str__(self):
        return self.title
