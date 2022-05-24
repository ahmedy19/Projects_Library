from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import magic
from accounts.models import Skill
from projects.models import Project, Tag


class DashboardUserCreationForm(UserCreationForm):

    username = forms.CharField(max_length=200, 
                          min_length=3,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 3 letters",
                            'placeholder':"Username",
                          }),
                          required=True,
                          label='Username',
                          strip=True,
                          error_messages={'required': 'Username is required with at least 3 letters'})
    

    first_name = forms.CharField(max_length=200, 
                          min_length=3,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 3 letters",
                            'placeholder':"First Name",
                          }),
                          required=True,
                          label='First Name',
                          strip=True,
                          error_messages={'required': 'First name is required with at least 3 letters'})

    last_name = forms.CharField(max_length=200, 
                          min_length=3,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 3 letters",
                            'placeholder':"Last Name",
                          }),
                          required=True,
                          label='Last Name',
                          strip=True,
                          error_messages={'required': 'Last name is required with at least 3 letters'})

    email = forms.CharField(max_length=200, 
                          min_length=18,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'email',
                            'help_text':"At least 18 letters",
                            'placeholder':"University Email",
                          }),
                          required=True,
                          label='University Email',
                          strip=True,
                          error_messages={'required': 'University email is required with at least 18 letters'})

    password1 = forms.CharField(max_length=200, 
                          min_length=10,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'password',
                            'help_text':"At least 10 letters",
                            'placeholder':"Password",
                          }),
                          required=True,
                          label='Password',
                          strip=True,
                          error_messages={'required': 'Password is required with at least 10 letters'})

    password2 = forms.CharField(max_length=200, 
                          min_length=10,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'password',
                            'help_text':"At least 10 letters",
                            'placeholder':"Confirm Password",
                          }),
                          required=True,
                          label='Confirm Password',
                          strip=True,
                          error_messages={'required': 'Password confirmation is required with at least 10 letters'})


    def clean_email(self):
        data = self.cleaned_data['email']
        if "@uoanbar.edu.iq" not in data:
            raise forms.ValidationError("Please, use your university email")
        return data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'University Email',
        }


class ProjectCreateForm(forms.ModelForm):

    title = forms.CharField(max_length=200, 
                          min_length=5,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 5 letters",
                            'placeholder':"Title",
                            'unique':True,
                          }),
                          required=True,
                          label='Title',
                          strip=True,
                          error_messages={'required': 'Title is required with at least 5 letters'})
    
    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(attrs={
                                        'class': 'form-control form-control-md',
                                        'type': 'text',
                                        'placeholder':"Description",
                                    }),
                                    required=True,
                                    strip=True,
                                    error_messages={'required': 'Description is required'})

    supervisor = forms.CharField(max_length=150, 
                          min_length=8,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 8 letters",
                            'placeholder':"Supervisor",
                          }),
                          required=True,
                          label='Supervisor',
                          strip=True,
                          error_messages={'required': 'Supervisor is required with at least 8 letters'})

    demo_link = forms.CharField(max_length=100, 
                          min_length=15,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 8 letters",
                            'placeholder':"Demo Link",
                          }),
                          required=True,
                          label='Demo Link',
                          strip=True,
                          error_messages={'required': 'Demo Link is required with at least 15 letters'})

    source_link = forms.CharField(max_length=2000, 
                          min_length=15,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 8 letters",
                            'placeholder':"Source Link",
                          }),
                          required=True,
                          label='Source Link',
                          strip=True,
                          error_messages={'required': 'Source Link is required with at least 15 letters'})
    

    project_image = forms.ImageField(label='Image',
                               widget=forms.FileInput(attrs={
                                    'class': 'input-group col-xs-12 file-upload-info file-upload-browse btn btn-primary',
                                    'type': 'file',
                                    'placeholder':"Upload Image",
                                }),
                                required=True,
                                error_messages={'required': 'Image is required'})

    project_file = forms.FileField(label='Project File',
                              widget=forms.FileInput(attrs={
                                    'class': 'input-group col-xs-12 file-upload-info file-upload-browse btn btn-primary',
                                    'type': 'file',
                                    'placeholder':"Upload Project File",
                                }),
                                required=True,
                                error_messages={'required': 'Project File is required'})

    tags = forms.ModelMultipleChoiceField(
                                queryset=Tag.objects.all(),
                                widget=forms.CheckboxSelectMultiple(attrs={
                                    'type': 'checkbox',
                                })
                              )
    


    def clean_file(self):
        file = self.cleaned_data.get("project_file", False)
        filetype = magic.from_buffer(file.read())
        if not "zip" in filetype:
            raise forms.ValidationError("File is not zip")
        return file


    class Meta:
        model = Project
        fields = ['title', 'description', 'supervisor', 'demo_link', 'source_link', 'project_image', 'project_file', 'tags']
        exclude = ['owner']



class TagCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=200, 
                          min_length=2,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 2 letters",
                            'placeholder':"Tag",
                          }),
                          required=True,
                          label='Tag',
                          strip=True,
                          error_messages={'required': 'Tag is required with at least 2 letters'})



    class Meta:
        model = Tag
        fields = '__all__'


class SkillCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=150, 
                          min_length=2,
                          widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'help_text':"At least 2 letters",
                            'placeholder':"Skill",
                          }),
                          required=True,
                          label='Skill',
                          strip=True,
                          error_messages={'required': 'Skill is required with at least 2 letters'})
    
    description = forms.CharField(label='Description',
                                  widget=forms.Textarea(attrs={
                                        'class': 'form-control form-control-md',
                                        'type': 'text',
                                        'placeholder':"Description",
                                    }),
                                    required=True,
                                    strip=True,
                                    error_messages={'required': 'Description is required'})



    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

