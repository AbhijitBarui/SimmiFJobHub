from django import forms
from .models import Jobs,Application

class JobsForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = '__all__'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['job','reviewed','accepted','job_id']