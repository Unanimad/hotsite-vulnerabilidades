from django import forms

from .models import *


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'process_number', 'version_stable', 'licenses_number', 'license_validity', 'note',
                  'provider', 'category']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'process_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'version_stable': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': Software._meta.get_field('version_stable').default
                }
            ),
            'licenses_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': Software._meta.get_field('licenses_number').default
                }
            ),
            'license_validity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': Software._meta.get_field('license_validity').default
                }
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'provider': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            )
        }


class VulnerabilityForm(forms.ModelForm):
    class Meta:
        model = Vulnerability
        fields = ['name', 'description', 'solution', 'severity', 'detected_at', 'products']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'solution': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'severity': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'detected_at': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'products': forms.Select(
                attrs={
                    'class': 'form-control',
                    'multiple': 'multiple',
                    'required': True,
                }
            )
        }
