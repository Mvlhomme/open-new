from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={
			'placeholder': 'Mot de passe'
		}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
			'placeholder': 'Confirmer votre mot de passe'
		}))


	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'email','pays', 'city', 'langue', 'devise', 'password']

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError(
				"Password does not match!"
			)

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['last_name'].widget.attrs['placeholder'] = 'Prenom'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['city'].widget.attrs['placeholder'] = 'City'
		self.fields['langue'].widget.attrs['placeholder'] = 'Langue'
		self.fields['pays'].widget.attrs['placeholder'] = 'Pays'
		self.fields['devise'].widget.attrs['placeholder'] = 'Devise'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):
	class Meta:
		model = Account 
		fields = ('first_name', 'last_name', 'city', 'pays', 'phone_number', 'langue')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control mb-4'


class UserProfileForm(forms.ModelForm):
	profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
	class Meta:
		model = UserProfile 
		fields = ('job', 'birthday', 'sexe', 'nationality', 'code_postale', 'adresse', 'profile_picture')

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control mb-4'