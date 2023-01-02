from django.db import models

class Contact(models.Model):
	nom = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	sujet = models.CharField(max_length=100)
	message = models.CharField(max_length=10000)

	#required
	date_send = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email 
