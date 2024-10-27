from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Return the name as the string representation

# CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    
    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return f'{self.car_make.name} {self.name}'  # Print car make and model