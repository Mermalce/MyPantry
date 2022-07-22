from django.db import models


# Create your models here.

class Item(models.Model):
    FRIG = 'FRIG'
    DESP = 'DESP'
    LOCAL_CHOICES = [
        (FRIG, 'Frigorifico'),
        (DESP, 'Despensa')
    ]

    LEG = 'LEG'
    LAC = 'LAC'
    CAT_CHOICES = [
        (LEG, 'Legume'),
        (LAC, 'Lacticinio')
    ]

    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=1)
    descricao = models.CharField(max_length=100, blank=True, default=' - ')
    data = models.DateField()
    local = models.CharField(max_length=5, choices=LOCAL_CHOICES, default=FRIG)
    categoria = models.CharField(max_length=5, choices=CAT_CHOICES, default=LEG)

    def __str__(self):
        return self.nome
