from django.db import models


class PriceCard(models.Model):
    price_card_value = models.CharField(max_length=20, verbose_name="Цена")

    def __str__(self):
        return self.price_card_value

    class Meta:
        verbose_name= 'Цена'
        verbose_name_plural = "Цены"


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=100, verbose_name='Услуга')
    pt_e = models.CharField(max_length=100, verbose_name='Еденица измерения')
    pt_old_price = models.CharField(max_length=100, verbose_name="Старая цена")
    pt_new_price = models.CharField(max_length=100, verbose_name="Новая цена")

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
