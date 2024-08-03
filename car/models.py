from django.utils import timezone

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CharField, PositiveIntegerField, TextField, ImageField, DateTimeField, \
    BooleanField, Manager


class AvailableCarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(car_status=Car.CarStatusChoices.ACTIVE)


class Car(models.Model):
    class BodyTypeChoices(models.TextChoices):
        SEDAN = 'седан', 'седан'
        HATCHBACK = 'хэтчбек', 'хэтчбек'
        UNIVERSAL = 'универсал', 'универсал'
        COUPE = 'купе', 'купе'
        CABRIOLET = 'кабриолет', 'кабриолет'
        ROADSTER = 'родстер', 'родстер'
        SUV = 'внедорожник', 'внедорожник'
        PICKUP = 'пикап', 'пикап'
        MINIVAN = 'минивэн', 'минивэн'
        VAN = 'фургон', 'фургон'
        LIMOUSINE = 'лимузин', 'лимузин'
        MICROBUS = 'микроавтобус', 'микроавтобус'

    class FuelChoices(models.TextChoices):
        DIESEL = 'дизель', 'дизель'
        GASOLINE = 'бензин', 'бензин'
        HYBRID = 'гибрид', 'гибрид'
        ELECTRIC = 'электро', 'электро'
        HYDROGEN = 'водород', 'водород'

    class DriveUnitChoices(models.TextChoices):
        FWD = 'FWD', 'FWD'
        RWD = 'RWD', 'RWD'
        FOUR_WD = '4WD', '4WD'

    class TransmissionChoices(models.TextChoices):
        AUTOMATIC = 'АКПП', 'АКПП'
        MANUAL = 'МКПП', 'МКПП'
        CVT = 'Вариатор', 'Вариатор'
        ROBOTIC = 'Робот', 'Робот'

    class CarStatusChoices(models.TextChoices):
        INACTIVE = '0', '0'
        ACTIVE = '1', '1'

    brand = CharField(max_length=64, verbose_name="brand")
    model = CharField(max_length=64, verbose_name="model")
    rent_deposit = PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="rent_deposit")
    body_type = CharField(max_length=64, choices=BodyTypeChoices.choices, verbose_name="body_type")
    drive_unit = CharField(max_length=32, choices=DriveUnitChoices.choices, verbose_name="drive_unit")
    fuel = CharField(max_length=32, choices=FuelChoices.choices, verbose_name="fuel")
    car_year = PositiveIntegerField(validators=[MinValueValidator(1971)], verbose_name="car_year")
    engine_power = PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name="engine_power")
    transmission = CharField(max_length=32, choices=TransmissionChoices.choices, verbose_name="transmission")
    description = TextField(verbose_name="description")
    car_number = CharField(max_length=64, verbose_name="car_number")
    car_photo = ImageField(upload_to='media/car_photos/', verbose_name="car_photo")
    car_status = BooleanField(default=True, verbose_name="car_status")
    time_create = DateTimeField(auto_now_add=True, verbose_name="time_create")

    objects = Manager()
    available = AvailableCarManager()

    class Meta:
        db_table = "cars"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'], name='idx_time_create')
        ]
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.car_year})"
