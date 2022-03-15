from django.forms import ModelForm
from django import forms
from .models import Project, Tag

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'supervisor', 'demo_link', 'source_link', 'project_image', 'project_file', 'tags']

        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple,
        # }

    tags = forms.ModelMultipleChoiceField(
    queryset=Tag.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'input input--text',
            'placeholder': 'Enter title',
            'type': 'text',
        })

        self.fields['supervisor'].widget.attrs.update({
            'class': 'input input--text',
            'placeholder': 'Enter supervisor name',
            'type': 'text',
        })

        self.fields['demo_link'].widget.attrs.update({
            'class': 'input input--text',
            'placeholder': 'Enter demo link',
            'type': 'text',
        })

        self.fields['source_link'].widget.attrs.update({
            'class': 'input input--text',
            'placeholder': 'Enter source code link',
            'type': 'text',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'input input--text',
            'placeholder': 'Write description'
        })




