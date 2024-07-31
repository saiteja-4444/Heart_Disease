from django import forms
from .models import UserPredictDataModel, DoctorFeedModel

class UserPredictDataForm(forms.ModelForm):
    class Meta():
        model = UserPredictDataModel
        fields = '__all__'

class DoctorFeedForm(forms.ModelForm):
    class Meta():
        model = DoctorFeedModel
        fields = '__all__'