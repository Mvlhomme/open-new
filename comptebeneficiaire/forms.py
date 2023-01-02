from django import forms
from .models import CompteBeneficiaire

class CompteBeneficiaireForm(forms.ModelForm):
	class Meta:
		model = CompteBeneficiaire 
		fields = ['nomBanque', 'nomBeneficiaire', 'iban', 'bic_swift', 'pays']

	def __init__(self, *args, **kwargs):
		super(CompteBeneficiaireForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control mb-4'
