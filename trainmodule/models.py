from django.db import models


class TrainModel(models.Model):
    number = models.IntegerField(
        unique=True, db_index=True, verbose_name="номер модели"
    )
    name = models.CharField(
        max_length=30, unique=True, db_index=True, verbose_name="название модели"
    )
    description = models.TextField(verbose_name="описание модели")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "модель"
        verbose_name_plural = "модели"
        ordering = [
            "number",
        ]
