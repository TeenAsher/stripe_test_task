from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)    # Цена в копейках

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def get_price(self):
        return '{0:.2f}'.format(self.price / 100)
