from django import forms

class GetVersionForm(forms.Form):
    
    which_app = forms.CharField(label="Which application do you want to compare: ", max_length=256)
    version_1 = forms.CharField(label='Input version 1 to get be compared against', max_length=100)
    version_2 = forms.CharField(label='Input version 2 to be compared against', max_length=100)
