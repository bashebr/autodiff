from django import forms

class GetVersionForm(forms.Form):
    whichapp = [
        ('magento', 'magento'),
        ('prestashop', 'prestashop'),
        ('wordpress', 'wordpress'),
        ('joomla', 'joomla')
    ]
    version1 = [
        ('2.3.2', 'Magento 2.3.2'),
        ('2.3.1', 'Magento 2.3.1'),
        ('2.3.0', 'Magento 2.3.0'),
        ('2.2.9', 'Magento 2.2.9'),
        ('2.2.8', 'Magento 2.2.8'),
        ('1.7.6.0', 'Prestashop 1.7.6.0'),
        ('1.7.5.2', 'Prestashop 1.7.5.2'),
        ('5.2.2', 'Wordpress 5.2.2'),
        ('5.2.1', 'Wordpress 5.2.1'),
        ('3.9.11', 'Joomla 3.9.11'),
        ('3.9.10', 'Joomla 3.9.10')
    ]
    which_app = forms.ChoiceField(choices=whichapp, label="Which application do you want to compare: ")

    version_1 = forms.ChoiceField(choices=version1, label='Input version 1 to get be compared against')
    version_2 = forms.ChoiceField(choices=version1, label='Input version 2 to be compared against')
