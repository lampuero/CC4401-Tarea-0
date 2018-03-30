from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="nombre_del_producto"
    )
    stock = models.IntegerField(
        default=5,
    )

    def add1(self):
        self.stock += 1

    def sub1(self):
        if self.stock >= 1:
            self.stock -= 1
