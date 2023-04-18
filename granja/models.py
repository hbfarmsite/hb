from django.db import models
from django.utils import timezone


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self) -> str:
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Raca(models.Model):
    nome = models.CharField(max_length=20)
    nome_cientifico = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
