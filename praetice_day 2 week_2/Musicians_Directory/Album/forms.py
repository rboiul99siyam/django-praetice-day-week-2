from django import forms 

from Album.models import add_album

class Album_form(forms.ModelForm):
   class Meta:
        model = add_album
        fields = '__all__'
        def clean(self):
                cleaned_data = super().clean()
                rating = cleaned_data['Album_rating']
                if rating < 5:
                    raise forms.ValidationError('Album readings can be given up to 5')
        widgets = {
                'Album_release_date':forms.DateTimeInput(attrs={'type':'datetime-local'})
            }