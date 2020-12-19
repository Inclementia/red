from django.db import models

class Managers(models.Model):
    name = models.CharField(max_length=200)
    competence = models.TextField(blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'
