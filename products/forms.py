from django.forms import ModelForm
from django import forms
from products.models import Review, Clothes, Order


class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class UpdateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'number']
