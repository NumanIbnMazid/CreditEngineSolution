from utils.mixins import CustomSimpleForm
from django import forms
from django_select2.forms import HeavySelect2Widget
from utils.views import get_city_data
from django.utils.translation import gettext as _



class WeatherForm(CustomSimpleForm):
    """
    Form for weather forecast
    """
    city = forms.ChoiceField(
        widget=HeavySelect2Widget(
            # data_url='get-city-data/',
            data_view=get_city_data,
            max_results=50,
            attrs={'data-minimum-input-length': '0'}
        ),
        required=True
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].label = _('City')
        self.fields['city'].help_text = _('Select city')
        self.fields['city'].error_messages = {'required': _('City is required')}
        self.fields['city'].required = True