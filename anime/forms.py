from django import forms
from .models import UserRating

class UserRatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ['user_name', 'rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }