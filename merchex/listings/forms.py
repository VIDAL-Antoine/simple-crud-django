from django import forms

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label='Nom')
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__'  
        exclude = ('active', 'official_homepage')
        labels = {
            'name': ('Nom'),
            'genre': ('Genre'),
            'biography': ('Biographie'),
            'year_formed': ('Année de création'),
            'active': ('Actif'),
            'official_homepage': ('Page officielle'),
        }

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        labels = {
            'title': ('Titre'),
            'description': ('Description'),
            'isSold': ('En vente'),
            'year': ('Année'),
            'type': ('Type'),
            'band': ('Groupe'),
        }