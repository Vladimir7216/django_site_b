from django.db import models


class StatusCrm(models.Model):
    status = models.CharField(max_length=200, verbose_name="Статус")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_data_time = models.DateTimeField(auto_now=True, verbose_name="Дата и время: ")
    order_name = models.CharField(max_length=200, verbose_name="Имя: ")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон: ")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, default="Новая", blank=True, verbose_name="Статус")

    order_address=models.CharField(max_length=200, null=True, verbose_name="Адрес объекта")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'


class ComentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")
    comment_text = models.TextField(max_length=2000, verbose_name="Коментарий по заказу")
    comment_dt = models.DateTimeField(auto_now=True, verbose_name="Дата и время заявки")

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
