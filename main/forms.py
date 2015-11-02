from django import forms

class Collage(forms.Form):
    user = forms.CharField(label='Користувач Twitter')
    width = forms.IntegerField(label='Ширина (в одиницях картинок)')
    height = forms.IntegerField(label='Висота (в одиницях картинок)')
