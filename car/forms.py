from django import forms

from car.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите марку'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите модель'}),
            'rent_deposit': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите депозит за аренду'}),
            'body_type': forms.Select(attrs={'class': 'form-control'}),
            'drive_unit': forms.Select(attrs={'class': 'form-control'}),
            'fuel': forms.Select(attrs={'class': 'form-control'}),
            'car_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите год выпуска'}),
            'engine_power': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите мощность двигателя'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'rows': 5}),
            'car_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер автомобиля'}),
            'car_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
