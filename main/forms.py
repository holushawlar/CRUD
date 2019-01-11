from django import forms
from .models import Goal


class GoalCreateForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            'title',
            'description',
            'created',
            'deadline'
        ]