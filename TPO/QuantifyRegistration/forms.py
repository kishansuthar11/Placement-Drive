from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'father_name', 'email', 'mobile', 'age', 'job_role', 'resume']
