from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CharField, PositiveIntegerField, TextField, URLField


class Car(models.Model):

    BODY_TYPE_CHOICES = [
        ('седан', 'седан'), ('хэтчбек', 'хэтчбек'), ('универсал', 'универсал'),
        ('купе', 'купе'), ('кабриолет', 'кабриолет'), ('родстер', 'родстер'),
        ('внедорожник', 'внедорожник'), ('пикап', 'пикап'), ('минивэн', 'минивэн'),
        ('фургон', 'фургон'), ('лимузин', 'лимузин'), ('микроавтобус', 'микроавтобус')
    ]

    CAR_FUEL_CHOICES = [
        ('дизель', 'дизель'), ('бензин', 'бензин'),
        ('гибрид', 'гибрид'), ('электро', 'электро'),
        ('водород', 'водород')
    ]

    DRIVE_UNIT_CHOICES = [
        ('FWD', 'FWD'), ('RWD', 'RWD'), ('4WD', '4WD')
    ]

    TRANSMISSION_CHOICES = [
        ('АКПП', 'АКПП'), ('МКПП', 'МКПП'),
        ('Вариатор', 'Вариатор'), ('Робот', 'Робот')
    ]

    CAR_STATUS_CHOICES = [
        ('0', '0'), ('1', '1')
    ]

    brand = CharField(max_length=64)
    model = CharField(max_length=64)
    rent_deposit = PositiveIntegerField(validators=[MinValueValidator(1)])
    body_type = CharField(max_length=64, choices=BODY_TYPE_CHOICES, default="седан")
    drive_unit = CharField(max_length=32, choices=DRIVE_UNIT_CHOICES)
    fuel = CharField(max_length=32, choices=CAR_FUEL_CHOICES)
    car_year = PositiveIntegerField(validators=[MinValueValidator(1971)])
    engine_power = PositiveIntegerField(validators=[MinValueValidator(1)])
    transmission = CharField(max_length=32, choices=TRANSMISSION_CHOICES)
    description = TextField()
    car_number = CharField(max_length=64)
    car_photo = URLField(max_length=256)
    car_status = CharField(max_length=1, choices=CAR_STATUS_CHOICES)

    class Meta:
        db_table = "cars"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.car_year})"
