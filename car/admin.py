from django.contrib import admin
from django.contrib.admin import ModelAdmin

from car.models import Car


class CarStatusFilter(admin.SimpleListFilter):
    title = "Статус автомобиля"
    parameter_name = "car_status"

    def lookups(self, request, model_admin):
        return [
            (Car.CarStatusChoices.ACTIVE, "1"),
            (Car.CarStatusChoices.INACTIVE, "0"),
        ]

    def queryset(self, request, queryset):
        if self.value() == Car.CarStatusChoices.ACTIVE:
            return queryset.filter(status=Car.CarStatusChoices.ACTIVE)
        if self.value() == Car.CarStatusChoices.INACTIVE:
            return queryset.filter(status=Car.CarStatusChoices.INACTIVE)
        return queryset


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = (
        'brand', 'model', 'rent_deposit', 'body_type', 'drive_unit', 'fuel',
        'car_year', 'engine_power', 'transmission', 'car_number', 'car_status', 'time_create', 'brief_info'
    )

    list_display_links = ('brand', 'model')
    ordering = ['time_create', 'brand']
    list_editable = (
        'rent_deposit', 'body_type', 'drive_unit', 'fuel',
        'car_year', 'engine_power', 'transmission', 'car_number', 'car_status'
    )
    search_fields = ('brand', 'model', 'car_number')
    list_filter = ('body_type', 'drive_unit', 'fuel', 'car_year', 'transmission')
    actions = ['change_status_1', 'change_status_0']
    fields = ['brand', 'model', 'rent_deposit', 'body_type', 'drive_unit', 'fuel',
              'car_year', 'engine_power', 'transmission', 'car_number', 'car_status']

    @admin.display(description="Длина описания автомобиля", ordering='content')
    def brief_info(self, car: Car):
        return f"Описание {len(car.description)} символов"

    @admin.action(description="Изменение статуса автомобиля (активный)")
    def change_status_1(self, request, queryset):
        count_updated = queryset.update(status=Car.CarStatusChoices.ACTIVE)
        self.message_user(request, f"Изменено {count_updated} записей")

    @admin.action(description="Изменение статуса автомобиля (неактивный)")
    def change_status_0(self, request, queryset):
        count_updated = queryset.update(status=Car.CarStatusChoices.INACTIVE)
        self.message_user(request, f"Изменено {count_updated} записей")
