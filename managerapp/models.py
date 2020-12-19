from django.db import models

class Managers(models.Model):
    name = models.CharField(max_length=200)
    competence = models.TextField(blank=True)
    photo = models.ImageField('Фото менеджера', upload_to='static/img', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
