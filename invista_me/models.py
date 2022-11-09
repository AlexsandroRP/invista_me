from django.db import models
from datetime import datetime
# Create your models here.

# Modelos que irão representar uma tabela no DB
class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)