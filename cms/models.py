from django.db import models


class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to="slider")
    cms_title = models.CharField(max_length=200, verbose_name="Заголовок")
    cms_text = models.TextField(max_length=2000, verbose_name="Текст")

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

