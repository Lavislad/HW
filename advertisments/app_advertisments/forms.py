from django import forms
from .models import Advertisement

class AdvertisementsForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }
    # title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    # price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    # auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'from-check-input'}), required=False)
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError("Заголовок не должен начинаться с вопросительного знака!")
        return title