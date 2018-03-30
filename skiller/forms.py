from django import forms
from .models import Skill, SkillData

class CreateSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['codename',]