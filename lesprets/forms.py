from django import forms
from .models import Demande_De_Pret

class DemandeDePretForm(forms.ModelForm):
	class Meta:
		model = Demande_De_Pret 
		fields = ['nom', 'email', 'telephone', 'whatsapp', 'pays', 'ville', 'montant_du_credit', 'duree_de_remboursement']