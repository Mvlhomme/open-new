from django.db import models

class Demande_De_Pret(models.Model):
	nom = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	telephone = models.CharField(max_length=100)
	whatsapp = models.CharField(max_length=100)
	pays = models.CharField(max_length=100)
	ville = models.CharField(max_length=1000)
	montant_du_credit = models.CharField(max_length=10000)
	duree_de_remboursement = models.CharField(max_length=10000)

	#required
	date_send = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email 
