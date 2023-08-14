from django import forms
from .models import User,Day,Diet
class UserForm(forms.Form):
    
    name = forms.ModelChoiceField(User.objects.all())
    day = forms.ChoiceField(choices = Day.Day_type_choices)

class AddPersonForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('__all__')

class AddDietForm(forms.ModelForm):
    diet = forms.CharField(max_length=100)
    class Meta:
        model = Diet
        fields=('diet',)

class DetailForm(forms.ModelForm):
    name = forms.ModelChoiceField(User.objects.all())
    class Meta:
        model = Day
        
        fields=['name','day','diet',]





     





    

    


    

    

