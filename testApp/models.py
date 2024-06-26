from django.db import models

# Create your models here.

#to afisame edwwwwwww

class PriceTanks(models.Model):
    TYPE = [
        ("10", "10"),
        ("13", "13"),
        ("25", "25"),
        ("0", "0"),
    ]
    tank_type = models.CharField(blank=True, max_length=2, choices=TYPE )

    price = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.tank_type


class GasTanks(models.Model):
    TYPE = [
        ("10", "10"),
        ("13", "13"),
        ("25", "25"),
    ]
    tank_type = models.CharField(blank=True, max_length=2, choices=TYPE )
    STATUS = [
        ("Full", "Full"),
        ("Empty", "Empty"),
        
    ]
    tank_status = models.CharField(default="Full", max_length=5, choices=STATUS )


    price = models.ForeignKey(PriceTanks,on_delete=models.CASCADE,default="10")


    def __str__(self):
        return self.tank_status+self.tank_type
    


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


