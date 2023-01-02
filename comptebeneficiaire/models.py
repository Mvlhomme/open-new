from django.db import models
from accounts.models import Account

class CompteBeneficiaire(models.Model):
	user = models.OneToOneField(Account, on_delete=models.CASCADE)
	nomBanque = models.CharField(blank=True, max_length=1000) 
	nomBeneficiaire = models.CharField(blank=True, max_length=1000)
	iban = models.CharField(blank=True, max_length=1000) 
	bic_swift = models.CharField(blank=True, max_length=1000) 
	pays = models.CharField(blank=True, max_length=1000)

	date_send = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nomBeneficiaire
