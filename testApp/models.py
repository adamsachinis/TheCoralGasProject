from django.db import models

# Create your models here.

#to afisame edwwwwwww


class GasTanks(models.Model):
    TYPE = [
        ("10", "10"),
        ("13", "13"),
        ("25", "25"),
    ]
    tank_type = models.CharField(blank=True, max_length=2, choices=TYPE )
    STATUS = [
        ("F", "Full"),
        ("E", "Empty"),
        
    ]
    tank_status = models.CharField(default="Full", max_length=1, choices=STATUS )
class PriceTanks(models.Model):
    TYPE = [
        ("10", "10"),
        ("13", "13"),
        ("25", "25"),
    ]
    tank_type = 
    models.CharField(blank=True, max_length=2, choices=TYPE )

            price = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.tank_typexzcxzcz


class Warehouse(models.Model):
    quantity_of_10_Full = models.ForeignKey(GasTanks,on_delete=models.CASCADE)
    quantity_of_13_Empty = models.PositiveIntegerField(GasTanks)
    quantity_of_13_Full = models.PositiveIntegerField(GasTanks)
    quantity_of_13_Empty = models.PositiveIntegerField(GasTanks)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    ANSWERS = [
        ("1", "s"),
        ("2", "unverified"),
        ("3", "unverified"),
        ("4", "unverified"),
    ]

    question_type = models.CharField(max_length=1, choices=ANSWERS , default="U")

#     pub_date = models.DateTimeField("date published")
#     likes = models.PositiveIntegerField("likes")
    # malakometer_quantity = models.TextChoices("poso", "LIGO METRIOS TERMA")
    # malakometer = models.CharField(blank=True, choices= malakometer_quantity,max_length=10)


