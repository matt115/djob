from django import forms
from .models import Skill, SkillData

class SkillDataForm(forms.ModelForm):
    error_css_class = 'alert alert-danger'

    class Meta:
        model = SkillData
        fields = ['_codename', 'description']

    def save(self, user, commit=True):
        skilldata = super(SkillDataForm, self).save(commit)
        Skill.objects.create(user=user, data=skilldata)
        return skilldata

class SkillSelectForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['data',]

