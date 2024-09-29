from django import forms
from .models import UserProfile
from .models import WorkExperience, Education, Certification
from .models import Project

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact_details']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company_name', 'description', 'start_date', 'end_date']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'institution', 'date_received']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

